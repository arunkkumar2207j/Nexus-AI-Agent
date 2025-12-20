import React, { useState, useRef, useEffect } from 'react';
import { Send, User, Bot, Loader2 } from 'lucide-react';
import { clsx } from 'clsx';
import AgentVisualizer from './AgentVisualizer';

interface Message {
    role: 'user' | 'assistant';
    content: string;
}

function ChatInterface() {
    const [messages, setMessages] = useState<Message[]>([]);
    const [input, setInput] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const [activeNode, setActiveNode] = useState<string>('idle');
    const scrollRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        scrollRef.current?.scrollIntoView({ behavior: 'smooth' });
    }, [messages]);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        if (!input.trim()) return;

        const userMsg: Message = { role: 'user', content: input };
        setMessages(prev => [...prev, userMsg]);
        setInput('');
        setIsLoading(true);
        setActiveNode('supervisor'); // Start visualization

        try {
            // Simulation of streaming steps for demo purposes
            // In real implementation, backend would stream SSE
            setTimeout(() => setActiveNode('researcher'), 1500);
            setTimeout(() => setActiveNode('writer'), 3500);

            const res = await fetch('http://localhost:8000/api/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: userMsg.content }),
            });

            const data = await res.json();

            setActiveNode('FINISH');
            setTimeout(() => setActiveNode('idle'), 2000);

            setMessages(prev => [...prev, { role: 'assistant', content: data.response }]);
        } catch (error) {
            console.error(error);
            setMessages(prev => [...prev, { role: 'assistant', content: `Error: ${error instanceof Error ? error.message : String(error)}` }]);
            setActiveNode('idle');
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="flex flex-col h-full bg-nexus-bg relative overflow-hidden font-sans">
            {/* Background Effects */}
            <div className="absolute top-0 left-0 w-full h-full pointer-events-none overflow-hidden">
                <div className="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] bg-nexus-accent/20 rounded-full blur-[100px]" />
                <div className="absolute bottom-[-10%] right-[-10%] w-[40%] h-[40%] bg-purple-500/20 rounded-full blur-[100px]" />
            </div>

            {/* Messages Area - Centered Channel */}
            <div className="flex-1 overflow-y-auto px-4 py-6 scroll-smooth z-10 w-full max-w-4xl mx-auto relative">
                {messages.length === 0 && (
                    <div className="flex flex-col items-center justify-center h-[80%] text-nexus-text-muted opacity-80">
                        <div className="p-6 bg-nexus-card/50 backdrop-blur-xl rounded-3xl border border-white/5 shadow-2xl mb-6">
                            <Bot className="w-16 h-16 text-nexus-accent" />
                        </div>
                        <h2 className="text-2xl font-bold text-nexus-text mb-2">Nexus Agent</h2>
                        <p className="text-sm">Powering intelligent conversations.</p>
                    </div>
                )}

                <div className="space-y-6 pb-24"> {/* Padding bottom for fixed footer */}
                    {messages.map((m, i) => (
                        <div key={i} className={clsx("flex gap-4 animate-in fade-in slide-in-from-bottom-4 duration-300", m.role === 'assistant' ? "flex-row" : "flex-row-reverse")}>
                            <div className={clsx("w-10 h-10 rounded-full flex items-center justify-center shrink-0 shadow-lg border border-white/10", m.role === 'assistant' ? "bg-nexus-card/80 backdrop-blur-md" : "bg-nexus-accent")}>
                                {m.role === 'assistant' ? <Bot size={20} className="text-nexus-accent" /> : <User size={20} className="text-white" />}
                            </div>
                            <div className={clsx("p-4 rounded-2xl max-w-[85%] text-sm leading-relaxed shadow-md backdrop-blur-sm",
                                m.role === 'assistant'
                                    ? "bg-nexus-card/80 border border-white/5 text-nexus-text rounded-tl-none"
                                    : "bg-gradient-to-br from-nexus-accent to-nexus-accent-hover text-white rounded-tr-none")}>
                                <p className="whitespace-pre-wrap">{m.content}</p>
                            </div>
                        </div>
                    ))}

                    {/* Loading Indicator */}
                    {isLoading && (
                        <div className="flex gap-4 animate-pulse">
                            <div className="w-10 h-10 rounded-full bg-nexus-card/50 flex items-center justify-center shrink-0 border border-white/5">
                                <Loader2 className="w-5 h-5 animate-spin text-nexus-accent" />
                            </div>
                            <div className="flex items-center gap-2 text-nexus-text-muted text-sm italic">
                                <span>Agent is thinking...</span>
                                {activeNode !== 'idle' && <span className="px-2 py-0.5 bg-nexus-card rounded text-xs border border-white/10 text-nexus-accent">{activeNode}</span>}
                            </div>
                        </div>
                    )}
                    <div ref={scrollRef} />
                </div>
            </div>

            {/* Input Footer - Single Line Fixed */}
            <div className="p-4 fixed bottom-0 left-0 w-full z-20 pointer-events-none">
                <div className="max-w-4xl mx-auto w-full pointer-events-auto">
                    <form onSubmit={handleSubmit} className="relative flex items-center gap-2 bg-nexus-card/80 backdrop-blur-xl border border-white/10 p-2 rounded-2xl shadow-2xl transition-all focus-within:border-nexus-accent/50 focus-within:ring-2 focus-within:ring-nexus-accent/20">
                        <input
                            type="text"
                            value={input}
                            onChange={(e) => setInput(e.target.value)}
                            placeholder="Type your message here..."
                            className="flex-1 bg-transparent border-none px-4 py-2 focus:outline-none text-nexus-text placeholder-gray-500 font-medium"
                            disabled={isLoading}
                        />
                        <button
                            type="submit"
                            disabled={isLoading || !input.trim()}
                            className="bg-nexus-accent hover:bg-nexus-accent-hover disabled:opacity-50 disabled:cursor-not-allowed text-white p-3 rounded-xl transition-all shadow-lg hover:shadow-nexus-accent/25"
                        >
                            <Send size={18} />
                        </button>
                    </form>
                    <div className="text-center mt-2">
                        <p className="text-[10px] text-nexus-text-muted opacity-50">Nexus AI Agent • v1.0 • Powering Next-Gen Intelligence</p>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default ChatInterface;
