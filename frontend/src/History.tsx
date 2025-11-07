import { useEffect, useState } from 'react';
import axios from 'axios';

export default function History() {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/history/')
      .then(res => setHistory(res.data));
  }, []);

  return (
    <div className="mt-8 p-6 bg-gray-50 rounded-xl">
      <h2 className="text-2xl font-bold mb-4">Your AI History</h2>
      {history.length === 0 ? (
        <p>No enhancements yet. Try the AI above!</p>
      ) : (
        <div className="space-y-4">
          {history.map((item: any) => (
            <div key={item.id} className="bg-white p-4 rounded-lg shadow">
              <p className="text-sm text-gray-500">{new Date(item.created_at).toLocaleString()}</p>
              <p className="font-semibold mt-2">Original: {item.original}</p>
              <p className="text-green-700 mt-1">Enhanced: {item.enhanced}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}