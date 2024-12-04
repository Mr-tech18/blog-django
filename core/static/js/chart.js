
const ctx = document.getElementById('myChart').getContext('2d');
new Chart(ctx, {
type: 'line', // Chart type (e.g., bar, line, pie, etc.)
data: {
    labels: ['January', 'February', 'March', 'April'], // X-axis labels
    datasets: [{
    label: 'Views',
    data: [65, 59, 80, 81], // Data points
    borderColor: 'rgba(75, 192, 192, 1)', // Line color
    borderWidth: 2, // Line thickness
    fill: false // Disable filling under the line
    }]
},
options: {
    responsive: true, // Chart adjusts to screen size
    scales: {
    y: {
        beginAtZero: true // Y-axis starts at 0
    }
    }
}
});

