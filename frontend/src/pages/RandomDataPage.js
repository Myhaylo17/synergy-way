import React, { useState } from 'react';
import { dataAPI } from '../services/api';

function RandomDataPage() {
  const [randomData, setRandomData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchRandomData = async () => {
    setLoading(true);
    try {
      const response = await dataAPI.getRandomData();
      setRandomData(response.data);
      setError(null);
    } catch (err) {
      setError('Failed to fetch random data: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page-container">
      <h2 className="page-title">Random Data</h2>

      {error && <div className="error-message">{error}</div>}

      <button onClick={fetchRandomData} disabled={loading}>
        {loading ? 'Loading...' : 'Get Random Data'}
      </button>

      {randomData && (
        <div style={{ marginTop: '2rem' }}>
          <h3>Random Data Result:</h3>
          <pre style={{
            background: '#f4f4f4',
            padding: '1rem',
            borderRadius: '4px',
            overflow: 'auto'
          }}>
            {JSON.stringify(randomData, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
}

export default RandomDataPage;