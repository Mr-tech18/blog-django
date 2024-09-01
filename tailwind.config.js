/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./core/templates/**/*.html",
    "./core/templates/partials/**/*.html",
    "./core/templates/templates_tags/**/*.html"
  
  ],
  theme: {
    extend: {},
    screens:{
      sm:'640px',
      md:'768px',
      lg:'1024px',
      xl:'1280px',
      'tablet':'1120px',
    }
  },
  plugins: [],
}

