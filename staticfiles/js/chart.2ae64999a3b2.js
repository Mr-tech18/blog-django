
const ctx = document.getElementById('myChart').getContext('2d');
new Chart(ctx, {
    type: 'pie', // Chart type (e.g., bar, line, pie, etc.)
    data: {
        labels: ['January', 'February', 'March', 'April'], // X-axis labels
        datasets: [{
            label: 'Views',
            data: [65, 59, 80, 81], // Data points
            backgroundColor:[
                'rgba(75, 10, 10, 1)',
                'rgba(30, 192, 192, 1)',
                'rgba(100, 102, 192, 1)',
                'rgba(32, 192, 10, 1)',
            ],
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

const ctx2 = document.getElementById('myChart2').getContext('2d');
new Chart(ctx2, {
type: 'bar', // Chart type (e.g., bar, line, pie, etc.)
data: {
    labels: ['January', 'February', 'March', 'April'], // X-axis labels
    datasets: [{
    label: 'Views',
    data: [65, 59, 80, 81], // Data points
    backgroundColor:[
        'rgba(75, 10, 10, 1)',
        'rgba(30, 192, 192, 1)',
        'rgba(100, 102, 192, 1)',
        'rgba(32, 192, 10, 1)',
        
    ],
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

