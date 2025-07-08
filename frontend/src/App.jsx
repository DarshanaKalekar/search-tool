import React, { useState } from 'react';

function App() {
  const [country, setCountry] = useState('IN');
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setResults([]);
    try {
      const res = await fetch('http://localhost:8000/search', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ country, query })
      });
      if (!res.ok) throw new Error('API error');
      const data = await res.json();
      setResults(data);
    } catch (err) {
      setError('Failed to fetch results.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: 600, margin: '2rem auto', fontFamily: 'sans-serif' }}>
      <h2>Product Price Search</h2>
      <form onSubmit={handleSubmit} style={{ marginBottom: 24 }}>
        <label>
          Country:
          <select value={country} onChange={e => setCountry(e.target.value)} style={{ marginLeft: 8 }}>
            <option value="IN">IN</option>
            <option value="US">US</option>
            <option value="UK">UK</option>
            <option value="CA">CA</option>
            <option value="AU">AU</option>
          </select>
        </label>
        <label style={{ marginLeft: 16 }}>
          Product:
          <input
            value={query}
            onChange={e => setQuery(e.target.value)}
            style={{ marginLeft: 8, width: 220 }}
            placeholder="e.g. iPhone 16 Pro, 128GB"
            required
          />
        </label>
        <button type="submit" style={{ marginLeft: 16 }}>Search</button>
      </form>
      {loading && <div>Loading...</div>}
      {error && <div style={{ color: 'red' }}>{error}</div>}
      {results.length > 0 && (
        <table border="1" cellPadding="8" style={{ width: '100%', borderCollapse: 'collapse' }}>
          <thead>
            <tr>
              <th>Product Name</th>
              <th>Price</th>
              <th>Currency</th>
              <th>Link</th>
            </tr>
          </thead>
          <tbody>
            {results.map((item, idx) => (
              <tr key={idx}>
                <td>{item.productName}</td>
                <td>{item.price}</td>
                <td>{item.currency}</td>
                <td><a href={item.link} target="_blank" rel="noopener noreferrer">View</a></td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default App;
