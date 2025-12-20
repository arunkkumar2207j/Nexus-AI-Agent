/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'nexus-bg': '#0f172a', // Deep slate
        'nexus-card': '#1e293b', // Lighter slate
        'nexus-card-hover': '#334155',
        'nexus-accent': '#6366f1', // Indigo
        'nexus-accent-hover': '#4f46e5',
        'nexus-text': '#f1f5f9', // Primary text
        'nexus-text-muted': '#94a3b8', // Secondary text
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
