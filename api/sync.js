const KV_GET_URL = 'https://keyvalue.immanuel.co/api/KeyVal/GetValue/r0g6lh3c/elena_30d_hex';
const KV_SET_BASE = 'https://keyvalue.immanuel.co/api/KeyVal/UpdateValue/r0g6lh3c/elena_30d_hex/';
const NTFY_URL = 'https://ntfy.sh/elena_vance_studio_sync_98234792';

export default async function handler(req, res) {
  res.setHeader('Cache-Control', 'no-store, no-cache, must-revalidate, proxy-revalidate');
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method === 'POST') {
    try {
      const body = typeof req.body === 'string' ? JSON.parse(req.body) : (req.body || {});
      const hex = (body.hex || '').replace(/[^0-9a-f]/gi, '').toLowerCase();
      if (hex.length !== 30) {
        return res.status(400).json({ ok: false, error: 'Invalid hex state' });
      }

      const payload = {
        clientId: body.clientId || 'server',
        hex,
        day: body.day || 1,
        label: body.label || 'Actualización',
        ts: body.ts || Date.now()
      };

      await Promise.allSettled([
        fetch(KV_SET_BASE + hex, { method: 'POST' }),
        fetch(NTFY_URL, {
          method: 'POST',
          body: JSON.stringify(payload)
        })
      ]);

      return res.status(200).json({ ok: true, hex, ts: payload.ts });
    } catch (err) {
      return res.status(500).json({ ok: false, error: String(err) });
    }
  }

  // GET request: fetch from both Ntfy history and KeyVal for maximum reliability
  try {
    const [kvRes, ntfyRes] = await Promise.allSettled([
      fetch(KV_GET_URL + '?t=' + Date.now(), { cache: 'no-store' }),
      fetch(NTFY_URL + '/json?poll=1&since=all', { cache: 'no-store' })
    ]);

    let latestHex = null;
    let latestTs = 0;

    if (ntfyRes.status === 'fulfilled' && ntfyRes.value.ok) {
      const text = await ntfyRes.value.text();
      const lines = text.trim().split('\n');
      for (const line of lines) {
        if (!line.trim()) continue;
        try {
          const evt = JSON.parse(line);
          if (evt.event === 'message' && evt.message) {
            const msg = JSON.parse(evt.message);
            if (msg.hex && msg.hex.length === 30 && (msg.ts || 0) >= latestTs) {
              latestHex = msg.hex;
              latestTs = msg.ts || (evt.time * 1000) || 1;
            }
          }
        } catch (e) {}
      }
    }

    if (kvRes.status === 'fulfilled' && kvRes.value.ok) {
      const kvText = (await kvRes.value.text()).replace(/"/g, '').trim();
      if (kvText.length === 30 && !latestHex) {
        latestHex = kvText;
      }
    }

    return res.status(200).json({
      ok: true,
      hex: latestHex || '000000000000000000000000000000',
      ts: latestTs
    });
  } catch (err) {
    return res.status(500).json({ ok: false, error: String(err) });
  }
}
