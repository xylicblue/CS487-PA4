const express = require('express');
const cors = require('cors');
const axios = require('axios');

const app = express();
app.use(cors());
app.use(express.json());
app.use(express.static('public'));

function normalizeAxiosError(err) {
    if (err.response) {
        return {
            status: err.response.status,
            message: err.response.data?.error || err.response.data || err.message,
        };
    }
    return { status: 500, message: err.message || 'Unexpected server error' };
}

// Proxy POST to Durable Function HTTP starter
app.post('/api/order', async (req, res) => {
    try {
        const funcUrl = process.env.FUNCTION_START_URL;
        if (!funcUrl) {
            return res.status(500).json({ error: 'FUNCTION_START_URL not configured' });
        }

        const { order_id, items } = req.body || {};
        if (!order_id || !Array.isArray(items) || items.length === 0) {
            return res.status(400).json({ error: 'Order payload must include order_id and at least one item' });
        }

        const response = await axios.post(funcUrl, req.body, { timeout: 30000 });
        res.json(response.data);
    } catch (err) {
        const normalized = normalizeAxiosError(err);
        console.error('Error starting orchestration:', normalized.message);
        res.status(normalized.status).json({ error: 'Failed to start order orchestration', details: normalized.message });
    }
});

// Proxy GET to Durable Function status URL
app.get('/api/status', async (req, res) => {
    try {
        const statusUrl = req.query.url;
        if (!statusUrl) {
            return res.status(400).json({ error: 'Missing status URL' });
        }

        const allowedStatusPrefix = process.env.FUNCTION_STATUS_URL;
        if (allowedStatusPrefix && !statusUrl.startsWith(allowedStatusPrefix)) {
            return res.status(400).json({ error: 'Status URL does not match FUNCTION_STATUS_URL' });
        }

        const response = await axios.get(statusUrl, { timeout: 30000 });
        res.json(response.data);
    } catch (err) {
        const normalized = normalizeAxiosError(err);
        console.error('Error fetching status:', normalized.message);
        res.status(normalized.status).json({ error: 'Failed to fetch status', details: normalized.message });
    }
});

const PORT = process.env.PORT || 8080;
const HOST = process.env.WEBSITE_SITE_NAME ? '0.0.0.0' : '127.0.0.1';
app.listen(PORT, HOST, () => console.log(`TaskFlow Web App running at http://${HOST}:${PORT}`));
