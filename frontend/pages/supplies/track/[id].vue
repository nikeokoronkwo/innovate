<script setup lang="ts">
const route = useRoute();

const item = ref({
  id: "123",
  name: "Sample Item",
  description: "This is a sample item for tracking analytics.",
});

const user = ref({
  id: "user-456",
  name: "John Doe",
});

const showDialog = ref(false); // Controls the visibility of the dialog

// Analytics data
const analyticsSummary = ref({
  views: 0,
  purchases: 0,
});

const analyticsData = ref([]); // Stores event data like view timestamps

// Sample data for the chart
const analyticsChartData = ref({
  labels: ["2025-03-28", "2025-03-29", "2025-03-30"],
  datasets: [
    {
      label: "Views",
      data: [12, 19, 10],
      fill: false,
      borderColor: "#42A5F5",
      tension: 0.1,
    },
    {
      label: "Purchases",
      data: [2, 3, 1],
      fill: false,
      borderColor: "#FF5733",
      tension: 0.1,
    },
  ],
});

// Track an item action (view, purchase)
const trackItemAction = (action) => {
  const trackingData = {
    userId: user.value.id,
    itemId: item.value.id,
    action: action,
    timestamp: new Date().toISOString(),
  };

  // Send the tracking data (could be a real API call here)
  sendAnalytics(trackingData);

  // Update analytics data
  updateAnalyticsSummary(action);
  updateChartData(action);
};

// Send analytics data (simulated here)
const sendAnalytics = (trackingData) => {
  console.log("Sending tracking data:", trackingData);
  // For example, send to a server here using fetch()
  // await fetch('/api/track-item', { method: 'POST', body: JSON.stringify(trackingData) });
};

// Update the summary (views, purchases)
const updateAnalyticsSummary = (action) => {
  if (action === "view") {
    analyticsSummary.value.views++;
  } else if (action === "purchase") {
    analyticsSummary.value.purchases++;
  }
};

// Update chart data (simulated)
const updateChartData = (action) => {
  const today = new Date().toISOString().split("T")[0]; // Current date in YYYY-MM-DD format
  const index = analyticsChartData.value.labels.indexOf(today);

  if (index === -1) {
    // Add a new entry for the current date if it doesn't exist
    analyticsChartData.value.labels.push(today);
    analyticsChartData.value.datasets[0].data.push(action === "view" ? 1 : 0);
    analyticsChartData.value.datasets[1].data.push(
      action === "purchase" ? 1 : 0,
    );
  } else {
    // Update the data for today
    const datasetIndex = action === "view" ? 0 : 1;
    analyticsChartData.value.datasets[datasetIndex].data[index]++;
  }
};
</script>

<template>
  <div>
    <Panel>
      <div>
        <div>
          <h1>Item Analytics</h1>
          <p>{{ item.description }}</p>

          <!-- Button to trigger item view and purchase tracking -->
          <Button
            label="Track Item View"
            icon="pi pi-eye"
            @click="trackItemAction('view')"
          />
          <Button
            label="Track Item Purchase"
            icon="pi pi-shopping-cart"
            @click="trackItemAction('purchase')"
          />

          <!-- Display Analytics Summary -->
          <div v-if="analyticsSummary">
            <h2>Analytics Summary</h2>
            <p>Views: {{ analyticsSummary.views }}</p>
            <p>Purchases: {{ analyticsSummary.purchases }}</p>
          </div>

          <!-- Button to show Analytics Details -->
          <Button
            label="Show Detailed Analytics"
            icon="pi pi-chart-bar"
            @click="showDialog = true"
          />

          <!-- Dialog with Detailed Analytics (e.g., Views Over Time) -->
          <Dialog
            header="Item Analytics Details"
            v-model:visible="showDialog"
            width="500px"
          >
            <div>
              <Chart type="line" :data="analyticsChartData" />
            </div>
          </Dialog>
        </div>
      </div>
    </Panel>
  </div>
</template>
