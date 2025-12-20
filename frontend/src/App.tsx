import React, { useState } from 'react';
import ChatInterface from './components/ChatInterface';
import AgentVisualizer from './components/AgentVisualizer';
import DocumentUpload from './components/DocumentUpload';

function App() {
  const [activeTab, setActiveTab] = useState<'chat' | 'docs'>('chat');

  return (
    <div className="bg-nexus-bg min-h-screen text-white font-sans selection:bg-nexus-accent selection:text-white">
      <header className="border-b border-white/10 p-4 flex items-center justify-between backdrop-blur-md bg-nexus-bg/50 sticky top-0 z-50">
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-full bg-gradient-to-tr from-blue-500 to-purple-600 animate-pulse"></div>
          <h1 className="text-xl font-bold tracking-tight">Nexus <span className="text-nexus-accent">AI Analyst</span></h1>
        </div>
        <nav className="flex gap-1 bg-white/5 p-1 rounded-lg">
          <button
            onClick={() => setActiveTab('chat')}
            className={`px-4 py-1.5 rounded-md text-sm font-medium transition-all ${activeTab === 'chat' ? 'bg-nexus-accent text-white shadow-lg' : 'hover:bg-white/10 text-gray-400'}`}
          >
            Mission Control
          </button>
          <button
            onClick={() => setActiveTab('docs')}
            className={`px-4 py-1.5 rounded-md text-sm font-medium transition-all ${activeTab === 'docs' ? 'bg-nexus-accent text-white shadow-lg' : 'hover:bg-white/10 text-gray-400'}`}
          >
            Knowledge Base
          </button>
        </nav>
      </header>

      <main className="container mx-auto p-6 max-w-7xl">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 h-[calc(100vh-8rem)]">
          {/* Main Workspace */}
          <div className="lg:col-span-8 bg-nexus-card rounded-2xl border border-white/5 overflow-hidden shadow-2xl flex flex-col">
            {activeTab === 'chat' ? <ChatInterface /> : <DocumentUpload />}
          </div>

          {/* Side Panel (Agent Internals) */}
          <div className="lg:col-span-4 flex flex-col gap-6">
            <div className="bg-nexus-card rounded-2xl border border-white/5 p-6 shadow-xl flex-1">
              <h2 className="text-sm font-semibold text-gray-400 uppercase tracking-wider mb-4 flex items-center gap-2">
                <span className="w-2 h-2 rounded-full bg-green-500 animate-ping"></span>
                Live Agent State
              </h2>
              <AgentVisualizer />
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
