/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./core/templates/**/*.html",
    "./core/templates/partials/**/*.html",
    "./core/templates/userauths/**/*.html",
    "./core/templates/templates_tags/**/*.html",
    "./author_page/templates/author_partial/**/*.html",
    "./author_page/templates/**/*.html",
  
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

