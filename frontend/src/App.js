import React, { useState } from 'react';
import ReactMarkdown from 'react-markdown';
import Spinner from './components/Spinner';
import useRoadmap from './hooks/useRoadmap';
import './index.css';
function App() {
  const [username, setUsername] = useState('');
  const { data, loading, error, generateRoadmap } = useRoadmap();

  const handleSubmit = (e) => {
    e.preventDefault();
    if (username.trim()) generateRoadmap(username);
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-50 to-gray-100 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-4xl mx-auto">
        
        {/* --- Hero Section --- */}
        <header className="text-center mb-12">
          <div className="inline-block px-4 py-1.5 mb-4 text-sm font-semibold tracking-wide text-blue-600 uppercase bg-blue-100 rounded-full">
            AI-Powered Career Growth
          </div>
          <h1 className="text-5xl font-extrabold text-gray-900 tracking-tight mb-4">
            Agentic Project <span className="text-blue-600">Architect</span>
          </h1>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto leading-relaxed">
            We analyze your GitHub repositories, cross-reference them with 2026 industry trends, 
            and build a personalized 4-week execution roadmap.
          </p>
        </header>

        {/* --- Feature Grid --- */}
        {!data && !loading && (
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
            {[
              { title: "Skill Analysis", desc: "Our Analyst Agent deep-dives into your code DNA.", icon: "🔍" },
              { title: "Trend Matching", desc: "Researcher Agent finds gaps in the current market.", icon: "📈" },
              { title: "Roadmap Design", desc: "Architect Agent builds your step-by-step plan.", icon: "🏗️" },
            ].map((feature, idx) => (
              <div key={idx} className="bg-white p-6 rounded-xl shadow-sm border border-gray-100 text-center hover:shadow-md transition">
                <div className="text-3xl mb-3">{feature.icon}</div>
                <h3 className="font-bold text-gray-800 mb-1">{feature.title}</h3>
                <p className="text-sm text-gray-500">{feature.desc}</p>
              </div>
            ))}
          </div>
        )}

        {/* --- Input Form --- */}
        <div className="bg-white p-2 rounded-2xl shadow-xl mb-10 border border-gray-100">
          <form onSubmit={handleSubmit} className="flex flex-col sm:flex-row gap-2">
            <div className="relative flex-1">
              <span className="absolute inset-y-0 left-0 pl-4 flex items-center text-gray-400">
                github.com/
              </span>
              <input
                type="text"
                className="w-full pl-28 pr-4 py-4 border-none rounded-xl focus:ring-2 focus:ring-blue-500 bg-gray-50 text-gray-900 font-medium"
                placeholder="Saad110jb"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
              />
            </div>
            <button
              type="submit"
              disabled={loading}
              className="bg-blue-600 text-white px-8 py-4 rounded-xl font-bold hover:bg-blue-700 disabled:bg-blue-300 transform active:scale-95 transition-all shadow-lg shadow-blue-200"
            >
              {loading ? "Architecting..." : "Generate Roadmap"}
            </button>
          </form>
        </div>

        {/* --- Loading State --- */}
        {loading && (
          <div className="text-center py-10 animate-fade-in">
            <Spinner />
            <div className="mt-6 space-y-2">
              <p className="text-lg font-medium text-blue-700 animate-pulse text-center w-full">
                Agents are collaborating on your plan...
              </p>
              <p className="text-sm text-gray-500 italic">
                (This usually takes 45-60 seconds due to multi-agent reasoning)
              </p>
            </div>
          </div>
        )}

        {/* --- Error State --- */}
        {error && (
          <div className="bg-red-50 border-l-4 border-red-500 p-4 mb-8 rounded-r-lg">
            <div className="flex items-center">
              <div className="text-red-500 font-bold mr-2">⚠️ Error:</div>
              <p className="text-red-700 text-sm font-medium">{error}</p>
            </div>
          </div>
        )}

        {/* --- Roadmap Result --- */}
        {data && (
          <div className="bg-white p-10 rounded-3xl shadow-2xl border border-gray-100 prose prose-blue max-w-none prose-headings:text-gray-900 prose-strong:text-blue-600 animate-slide-up">
            <div className="flex justify-between items-center mb-8 border-b pb-4">
              <h2 className="text-2xl font-bold text-gray-800 m-0">Your Personalized Roadmap</h2>
              <button 
                onClick={() => window.print()} 
                className="text-sm text-gray-400 hover:text-blue-600 transition font-medium"
              >
                Download PDF
              </button>
            </div>
            <ReactMarkdown>{data}</ReactMarkdown>
          </div>
        )}
        
        {/* --- Footer --- */}
        <footer className="mt-20 text-center text-gray-400 text-sm">
          <p>© 2026 Agentic Project Architect • Built with CrewAI & Groq LPU</p>
        </footer>
      </div>
    </div>
  );
}

export default App;