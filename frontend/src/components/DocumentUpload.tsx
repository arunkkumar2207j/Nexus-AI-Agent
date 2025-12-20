import React, { useState } from 'react';
import { Upload, FileText, Check, AlertCircle } from 'lucide-react';
import { motion } from 'framer-motion';

function DocumentUpload() {
    const [isDragging, setIsDragging] = useState(false);
    const [uploadStatus, setUploadStatus] = useState<'idle' | 'uploading' | 'success' | 'error'>('idle');
    const [message, setMessage] = useState('');

    const handleFile = async (file: File) => {
        if (file.type !== 'application/pdf') {
            setUploadStatus('error');
            setMessage('Only PDF files are supported.');
            return;
        }

        setUploadStatus('uploading');
        setMessage(`Uploading ${file.name}...`);

        const formData = new FormData();
        formData.append('file', file);

        try {
            const res = await fetch('http://localhost:8000/api/upload', {
                method: 'POST',
                body: formData,
            });

            if (!res.ok) throw new Error('Upload failed');

            const data = await res.json();
            setUploadStatus('success');
            setMessage(data.message);
        } catch (e) {
            setUploadStatus('error');
            setMessage('Failed to upload document. Is the backend running?');
        }
    };

    return (
        <div className="flex flex-col items-center justify-center h-full p-12">
            <motion.div
                className={`w-full max-w-xl h-64 border-2 border-dashed rounded-3xl flex flex-col items-center justify-center cursor-pointer transition-colors ${isDragging ? 'border-nexus-accent bg-nexus-accent/10' : 'border-white/20 hover:border-white/40'}`}
                onDragOver={(e) => { e.preventDefault(); setIsDragging(true); }}
                onDragLeave={() => setIsDragging(false)}
                onDrop={(e) => {
                    e.preventDefault();
                    setIsDragging(false);
                    const file = e.dataTransfer.files[0];
                    if (file) handleFile(file);
                }}
                onClick={() => document.getElementById('file-upload')?.click()}
            >
                <input
                    type="file"
                    id="file-upload"
                    className="hidden"
                    accept="application/pdf"
                    onChange={(e) => e.target.files?.[0] && handleFile(e.target.files[0])}
                />

                {uploadStatus === 'idle' && (
                    <>
                        <div className="w-16 h-16 bg-nexus-card rounded-full flex items-center justify-center mb-4 border border-white/10">
                            <Upload className="text-nexus-accent w-8 h-8" />
                        </div>
                        <p className="text-xl font-medium mb-1">Upload Knowledge</p>
                        <p className="text-gray-500">Drag & drop PDF or click to browse</p>
                    </>
                )}

                {uploadStatus === 'uploading' && (
                    <div className="flex flex-col items-center animate-pulse">
                        <FileText className="w-12 h-12 text-nexus-accent mb-4" />
                        <p className="text-lg">Ingesting Knowledge Base...</p>
                    </div>
                )}

                {uploadStatus === 'success' && (
                    <div className="flex flex-col items-center">
                        <Check className="w-12 h-12 text-green-500 mb-4" />
                        <p className="text-lg text-green-400">Knowledge Ingested</p>
                    </div>
                )}

                {uploadStatus === 'error' && (
                    <div className="flex flex-col items-center">
                        <AlertCircle className="w-12 h-12 text-red-500 mb-4" />
                        <p className="text-lg text-red-400">Upload Failed</p>
                    </div>
                )}
            </motion.div>

            {message && <p className="mt-4 text-gray-400 font-mono text-sm">{message}</p>}
        </div>
    );
}

export default DocumentUpload;
