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
        fetch(KV_SET_BASE + hex, {
          method: 'POST',
          headers: { 'Content-Length': '0' },
          body: ''
        }),
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

  // GET request: fetch authoritative state from KeyVal
  try {
    const kvRes = await fetch(KV_GET_URL, { cache: 'no-store' });
    if (kvRes.ok) {
      const kvText = (await kvRes.text()).replace(/"/g, '').trim();
      if (kvText.length === 30) {
        return res.status(200).json({ ok: true, hex: kvText, ts: Date.now() });
      }
    }

    return res.status(200).json({
      ok: true,
      hex: '000000000000000000000000000000',
      ts: 0
    });
  } catch (err) {
    return res.status(500).json({ ok: false, error: String(err) });
  }
}
