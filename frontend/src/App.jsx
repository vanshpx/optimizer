import { useState, useEffect } from 'react'

function App() {
    const [data, setData] = useState(null)

    useEffect(() => {
        // This fetches from the backend via the Vite proxy configured in vite.config.js
        fetch('/api/')
            .then(res => res.json())
            .then(data => setData(data))
            .catch(err => console.error('Error fetching from backend:', err))
    }, [])

    return (
        <div style={{ padding: '2rem', fontFamily: 'system-ui, sans-serif', maxWidth: '800px', margin: '0 auto' }}>
            <h1>TBO Agent System</h1>
            <div style={{ padding: '1rem', border: '1px solid #ccc', borderRadius: '8px', marginTop: '1rem' }}>
                <h2>Backend Connectivity</h2>
                <p>
                    Status: <strong>{data ? 'Connected' : 'Connecting...'}</strong>
                </p>
                {data && (
                    <pre style={{ background: '#f5f5f5', padding: '1rem', borderRadius: '4px' }}>
                        {JSON.stringify(data, null, 2)}
                    </pre>
                )}
            </div>
            <p style={{ marginTop: '2rem', color: '#666' }}>
                Edit <code>frontend/src/App.jsx</code> to start building your UI.
            </p>
        </div>
    )
}

export default App
