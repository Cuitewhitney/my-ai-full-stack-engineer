import { useState } from 'react';
import axios from 'axios';
import History from './History';

function App() {
  const [input, setInput] = useState('');
  const [output, setOutput] = useState('');
  const [loading, setLoading] = useState(false);

    const enhance = async () => {
    if (!input.trim()) return;
    setLoading(true);
    try {
      // DYNAMIC API URL – works on localhost AND Railway
      const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000/api/';
      const res = await axios.post(`${API_URL}enhance/`, {
        text: input
      });
      setOutput(res.data.enhanced);
    } catch (err: any) {
      setOutput('Backend not running – check Railway logs or run locally with: python manage.py runserver');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-purple-50 p-8">
      <div className="max-w-2xl mx-auto">
        <h1 className="text-4xl font-bold text-center mb-8 text-purple-800">
          AI Text Enhancer
        </h1>
        
        <textarea
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type anything..."
          className="w-full p-5 border-2 border-purple-300 rounded-xl text-lg focus:outline-none focus:border-purple-600"
          rows={6}
        />

        <button
          onClick={enhance}
          disabled={loading}
          className="mt-6 w-full bg-gradient-to-r from-purple-600 to-blue-600 text-white py-4 rounded-xl font-bold text-xl hover:shadow-2xl disabled:opacity-70"
        >
          {loading ? 'AI Thinking...' : 'ENHANCE WITH AI'}
        </button>

        {output && (
          <div className="mt-8 p-6 bg-white rounded-xl shadow-lg">
            <p className="text-sm font-semibold text-purple-700 mb-2">AI Result:</p>
            <p className="whitespace-pre-wrap text-gray-800">{output}</p>
          </div>
        )}
      </div>
      <History />
    </div>
  );
}

export default App;