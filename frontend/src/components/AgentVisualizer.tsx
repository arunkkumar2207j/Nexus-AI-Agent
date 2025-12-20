import React from 'react';
import { motion } from 'framer-motion';
import { Brain, Search, PenTool, CheckCircle } from 'lucide-react';
import { clsx } from 'clsx';

const nodes = [
    { id: 'supervisor', label: 'Supervisor', icon: Brain, color: 'text-purple-400', border: 'border-purple-500/50' },
    { id: 'researcher', label: 'Researcher', icon: Search, color: 'text-blue-400', border: 'border-blue-500/50' },
    { id: 'writer', label: 'Writer', icon: PenTool, color: 'text-amber-400', border: 'border-amber-500/50' },
    { id: 'FINISH', label: 'Done', icon: CheckCircle, color: 'text-green-400', border: 'border-green-500/50' },
];

function AgentVisualizer({ activeNode = 'supervisor' }: { activeNode?: string }) {
    return (
        <div className="relative h-64 w-full flex flex-col items-center justify-center p-4">
            {/* Connector Lines (SVG) */}
            <svg className="absolute inset-0 w-full h-full pointer-events-none stroke-white/20" strokeWidth="2">
                <line x1="50%" y1="20%" x2="25%" y2="50%" />
                <line x1="50%" y1="20%" x2="75%" y2="50%" />
                <line x1="25%" y1="50%" x2="50%" y2="80%" />
                <line x1="75%" y1="50%" x2="50%" y2="80%" />
            </svg>

            {/* Supervisor Node */}
            <div className="absolute top-[10%] left-1/2 -translate-x-1/2">
                <Node id="supervisor" active={activeNode === 'supervisor'} />
            </div>

            {/* Researcher Node */}
            <div className="absolute top-[50%] left-[20%]">
                <Node id="researcher" active={activeNode === 'researcher'} />
            </div>

            {/* Writer Node */}
            <div className="absolute top-[50%] right-[20%]">
                <Node id="writer" active={activeNode === 'writer'} />
            </div>

            {/* Finish Node */}
            <div className="absolute bottom-[10%] left-1/2 -translate-x-1/2">
                <Node id="FINISH" active={activeNode === 'FINISH'} />
            </div>
        </div>
    );
}

function Node({ id, active }: { id: string, active: boolean }) {
    const node = nodes.find(n => n.id === id) || nodes[0];
    const Icon = node.icon;

    return (
        <motion.div
            animate={{ scale: active ? 1.1 : 1, opacity: active ? 1 : 0.6 }}
            className={clsx(
                "bg-nexus-bg p-3 rounded-xl border-2 flex flex-col items-center gap-2 shadow-2xl z-10 w-24",
                active ? `${node.border} shadow-[0_0_20px_rgba(0,0,0,0.5)]` : "border-white/10"
            )}
        >
            <Icon className={clsx("w-6 h-6", active ? node.color : "text-gray-500")} />
            <span className={clsx("text-xs font-bold", active ? "text-white" : "text-gray-500")}>
                {node.label}
            </span>
            {active && (
                <span className="absolute -top-1 -right-1 flex h-3 w-3">
                    <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-nexus-accent opacity-75"></span>
                    <span className="relative inline-flex rounded-full h-3 w-3 bg-nexus-accent"></span>
                </span>
            )}
        </motion.div>
    );
}

export default AgentVisualizer;
