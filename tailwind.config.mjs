/** @type {import('tailwindcss').Config} */
import typography from '@tailwindcss/typography'

export default {
	content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
	darkMode: "class",
	theme: {
		fontFamily: {
			'mono': ['Space Mono', 'monospace']
		},
		extend: {
			colors: {
				bgColor: "var(--theme-bg)",
				textColor: "var(--theme-text)",
				link: "var(--theme-link)",
				accent: "var(--theme-accent)",
				"accent-2": "var(--theme-accent-2)",
				surface: "var(--theme-surface)",
				quote: "var(--theme-quote)",
				highlight: "var(--theme-highlight)"
			},
			typography: {
				quoteless: {
					css: {
						'blockquote p:first-of-type::before': { content: 'none' },
						'blockquote p:first-of-type::after': { content: 'none' },
					},
				},
			},
		}
	},
	plugins: [
		typography,
	],
}
