// import { useEffect, useState } from 'react';
// import axios from 'axios';

// export default function History() {
//   const [history, setHistory] = useState([]);

//   useEffect(() => {
//     axios.get('http://127.0.0.1:8000/api/history/')
//       .then(res => setHistory(res.data));
//   }, []);

//   return (
//     <div className="mt-8 p-6 bg-gray-50 rounded-xl">
//       <h2 className="text-2xl font-bold mb-4">Your AI History</h2>
//       {history.length === 0 ? (
//         <p>No enhancements yet. Try the AI above!</p>
//       ) : (
//         <div className="space-y-4">
//           {history.map((item: any) => (
//             <div key={item.id} className="bg-white p-4 rounded-lg shadow">
//               <p className="text-sm text-gray-500">{new Date(item.created_at).toLocaleString()}</p>
//               <p className="font-semibold mt-2">Original: {item.original}</p>
//               <p className="text-green-700 mt-1">Enhanced: {item.enhanced}</p>
//             </div>
//           ))}
//         </div>
//       )}
//     </div>
//   );
// }

import { useEffect, useState } from 'react';
import axios from 'axios';

export default function History() {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    fetchHistory();
  }, []);

  const fetchHistory = async () => {
    try {
      const res = await axios.get('http://127.0.0.1:8000/api/history/');
      setHistory(res.data);
    } catch (err) {
      console.log('No history yet');
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