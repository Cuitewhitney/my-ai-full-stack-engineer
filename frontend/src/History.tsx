import { useEffect, useState } from 'react';
import axios from 'axios';

export default function History() {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    fetchHistory();
  }, []);

  const fetchHistory = async () => {
    try {
      // DYNAMIC API URL – works on localhost AND Railway
      const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000/api/';
      const res = await axios.get(`${API_URL}history/`);
      setHistory(res.data);
    } catch (err) {
      console.log('No history yet or backend not connected');
    }
  };

  return (
    <div className="mt-8 p-4 bg-gray-100 rounded-lg">
      <h2 className="text-xl font-bold mb-4">Your AI History</h2>
      {history.length === 0 ? (
        <p>No enhancements yet. Try one!</p>
      ) : (
        <ul>
          {history.map((item: any) => (
            <li key={item.id} className="mb-4 border-b pb-2">
              <p><strong>Original:</strong> {item.original}</p>
              <p><strong>Enhanced:</strong> {item.enhanced}</p>
              <p className="text-sm text-gray-500">{new Date(item.created_at).toLocaleString()}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}