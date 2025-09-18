document.addEventListener('DOMContentLoaded', function() {
  // Grab JSON from hidden script tags
  const riskDataText = document.getElementById('riskData').textContent;
  const trendsDataText = document.getElementById('trendsData').textContent;

  let riskData = [];
  let trendsData = [];

  try {
    riskData = JSON.parse(riskDataText);
    trendsData = JSON.parse(trendsDataText);
  } catch (e) {
    console.error("Invalid JSON in riskData or trendsData script tag!", e);
    return;
  }

  // Pie chart data setup
  const labels = riskData.map(item => item._id || 'High');
  const counts = riskData.map(item => item.count);
  const bgColors = ['#53c28b', '#f8b26a', '#f38f66', '#37a2da', '#9fe6b8'];

  // Render Pie Chart
  if (document.getElementById('riskPieChart')) {
    const ctxPie = document.getElementById('riskPieChart').getContext('2d');
    new Chart(ctxPie, {
      type: 'pie',
      data: {
        labels: labels,
        datasets: [{
          data: counts,
          backgroundColor: bgColors,
        }]
      },
      options: {
        responsive: true,
        plugins: {
          legend: { position: 'bottom' }
        }
      }
    });
  }

  // Prepare Line Chart for Readmission Trends (last 30 days)
  const trendLabels = trendsData.map(item => {
    const d = item._id;
    if (!d) return '';
    return `${d.day}/${d.month}/${d.year}`;
  });
  const trendCounts = trendsData.map(item => item.count);

  // Render Line Chart
  if (document.getElementById('readmissionTrendChart')) {
    const ctxLine = document.getElementById('readmissionTrendChart').getContext('2d');
    new Chart(ctxLine, {
      type: 'line',
      data: {
        labels: trendLabels,
        datasets: [{
          label: 'Readmissions',
          data: trendCounts,
          fill: false,
          borderColor: '#37a2da',
          tension: 0.1
        }]
      },
      options: {
        responsive: true,
        scales: {
          y: { beginAtZero: true, precision: 0 }
        }
      }
    });
  }
});
