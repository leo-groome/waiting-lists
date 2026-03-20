<script setup lang="ts">
import { onMounted } from 'vue';
import { useWaitingListStore } from '../stores/waitingList';
import WaitingListTable from '../components/WaitingListTable.vue';

const store = useWaitingListStore();

onMounted(() => {
  store.fetchAllLists();
});

const refreshData = () => {
  store.fetchAllLists();
};
</script>

<template>
  <div class="dashboard">
    <header class="dashboard-header">
      <div class="header-content">
        <h1>Waiting Lists Dashboard</h1>
        <p class="subtitle">Monitor and manage your general and exclusive registers.</p>
      </div>
      <button @click="refreshData" :disabled="store.loading" class="refresh-btn">
        <span v-if="store.loading" class="spinner-sm"></span>
        {{ store.loading ? 'Refreshing...' : 'Refresh Data' }}
      </button>
    </header>

    <div v-if="store.error" class="error-banner">
      <p>{{ store.error }}</p>
    </div>

    <div class="dashboard-grid">
      <section class="general-section">
        <WaitingListTable 
          title="General Waiting List" 
          :items="store.sortedGeneralList" 
          :loading="store.loading"
        />
      </section>

      <section class="exclusive-section">
        <WaitingListTable 
          title="Exclusive Waiting List" 
          :items="store.sortedExclusiveList" 
          :loading="store.loading"
        />
      </section>
    </div>
  </div>
</template>

<style scoped>
.dashboard {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.dashboard-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: 3rem;
  gap: 1rem;
}

h1 {
  font-size: 2.5rem;
  font-weight: 800;
  background: linear-gradient(135deg, #fff 0%, #a1a1aa 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin: 0 0 0.5rem 0;
}

.subtitle {
  color: #71717a;
  font-size: 1.125rem;
}

.refresh-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: #6366f1;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 0.75rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.refresh-btn:hover:not(:disabled) {
  background: #4f46e5;
  transform: translateY(-1px);
}

.refresh-btn:active:not(:disabled) {
  transform: translateY(0);
}

.refresh-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.dashboard-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
}

.error-banner {
  background: rgba(239, 68, 68, 0.1);
  color: #ef4444;
  padding: 1rem;
  border-radius: 0.75rem;
  margin-bottom: 2rem;
  border: 1px solid rgba(239, 68, 68, 0.2);
}

.spinner-sm {
  width: 1rem;
  height: 1rem;
  border: 2px solid rgba(255, 255, 255, 0.2);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

@media (max-width: 768px) {
  .dashboard {
    padding: 1rem;
  }

  .dashboard-header {
    flex-direction: column;
    align-items: flex-start;
    margin-bottom: 2rem;
  }

  h1 {
    font-size: 1.75rem;
  }

  .subtitle {
    font-size: 0.875rem;
  }

  .refresh-btn {
    width: 100%;
    justify-content: center;
  }
}

@media (min-width: 1024px) {
  .dashboard-grid {
    grid-template-columns: 1fr 1fr;
  }
}
</style>
