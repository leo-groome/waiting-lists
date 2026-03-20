<script setup lang="ts">
import { ref, computed } from 'vue';
import { type WaitingListEntry } from '../services/WaitingListService';

const props = defineProps<{
  title: string;
  items: WaitingListEntry[];
  loading: boolean;
}>();

const filterPlan = ref<string>('all');
const sortOrder = ref<'newest' | 'oldest'>('newest');
const showCopyToast = ref(false);

const filteredAndSortedItems = computed(() => {
  let result = [...props.items];

  // Filter by plan
  if (filterPlan.value !== 'all') {
    result = result.filter(item => item.plan_type === filterPlan.value);
  }

  // Sort
  result.sort((a, b) => {
    const dateA = new Date(a.created_at).getTime();
    const dateB = new Date(b.created_at).getTime();
    return sortOrder.value === 'newest' ? dateB - dateA : dateA - dateB;
  });

  return result;
});

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleString('en-US', {
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  });
};

const getPlanClass = (plan: string) => {
  return `plan-badge plan-${plan}`;
};

const copyEmail = async (email: string) => {
  try {
    await navigator.clipboard.writeText(email);
    showCopyToast.value = true;
    setTimeout(() => {
      showCopyToast.value = false;
    }, 2000);
  } catch (err) {
    console.error('Failed to copy text: ', err);
  }
};

const getWhatsAppLink = (phone: string) => {
  // Remove non-numeric characters for WhatsApp link
  const cleanPhone = phone.replace(/\D/g, '');
  return `https://wa.me/${cleanPhone}`;
};
</script>

<template>
  <div class="list-container glass">
    <div class="list-header">
      <div class="header-left">
        <h2>{{ title }}</h2>
        <span class="count">{{ filteredAndSortedItems.length }} results</span>
      </div>
      
      <div class="controls">
        <select v-model="filterPlan" class="control-select">
          <option value="all">All Plans</option>
          <option value="basic">Basic</option>
          <option value="standard">Standard</option>
          <option value="pro">Pro</option>
        </select>

        <select v-model="sortOrder" class="control-select">
          <option value="newest">Newest First</option>
          <option value="oldest">Oldest First</option>
        </select>
      </div>
    </div>

    <div v-if="loading" class="loading-state">
      <div class="spinner"></div>
      <p>Loading entries...</p>
    </div>

    <div v-else-if="filteredAndSortedItems.length === 0" class="empty-state">
      <p v-if="items.length > 0">No registers match this filter.</p>
      <p v-else>No registers found in this list yet.</p>
    </div>

    <div v-else class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Plan</th>
            <th>Registered</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in filteredAndSortedItems" :key="item.id" class="row-entry">
            <td class="name-cell" data-label="Name">{{ item.name }}</td>
            <td class="email-cell" data-label="Email">
              <div class="email-wrapper">
                <span>{{ item.email }}</span>
                <button @click="copyEmail(item.email)" class="icon-btn" title="Copy Email">
                  <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
                </button>
              </div>
            </td>
            <td data-label="Phone">
              <a :href="getWhatsAppLink(item.phone)" target="_blank" class="phone-link" title="Chat on WhatsApp">
                <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="wa-icon"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
                {{ item.phone }}
              </a>
            </td>
            <td data-label="Plan">
              <span :class="getPlanClass(item.plan_type)">
                {{ item.plan_type }}
              </span>
            </td>
            <td class="date-cell" data-label="Registered">{{ formatDate(item.created_at) }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <Transition name="fade">
      <div v-if="showCopyToast" class="toast">Email copied!</div>
    </Transition>
  </div>
</template>

<style scoped>
.list-container {
  padding: 1.5rem;
  border-radius: 1.25rem;
  border: 1px solid rgba(255, 255, 255, 0.1);
  background: rgba(20, 20, 25, 0.6);
  backdrop-filter: blur(12px);
  margin-bottom: 2rem;
  transition: transform 0.3s ease;
  position: relative;
}

.list-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  flex-wrap: wrap;
  gap: 1rem;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

h2 {
  font-size: 1.25rem;
  font-weight: 600;
  color: #fff;
  margin: 0;
}

.count {
  font-size: 0.75rem;
  color: #a1a1aa;
  background: rgba(255, 255, 255, 0.05);
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
}

.controls {
  display: flex;
  gap: 0.5rem;
}

.control-select {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: #e4e4e7;
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  font-size: 0.875rem;
  cursor: pointer;
  outline: none;
}

.control-select:focus {
  border-color: #6366f1;
}

.table-wrapper {
  overflow-x: auto;
}

table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
}

th {
  padding: 0.75rem 1rem;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: #71717a;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

td {
  padding: 1rem;
  font-size: 0.875rem;
  color: #e4e4e7;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.row-entry {
  transition: background 0.2s ease;
}

.row-entry:hover {
  background: rgba(255, 255, 255, 0.03);
}

.name-cell {
  font-weight: 500;
  color: #fff;
}

.email-wrapper {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.icon-btn {
  background: transparent;
  border: none;
  color: #71717a;
  cursor: pointer;
  padding: 0.25rem;
  display: flex;
  align-items: center;
  border-radius: 0.25rem;
  transition: all 0.2s;
}

.icon-btn:hover {
  color: #fff;
  background: rgba(255, 255, 255, 0.1);
}

.phone-link {
  color: #a1a1aa;
  text-decoration: none;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: color 0.2s;
}

.phone-link:hover {
  color: #22c55e;
}

.wa-icon {
  color: #22c55e;
}

.email-cell {
  color: #a1a1aa;
}

.date-cell {
  white-space: nowrap;
  color: #71717a;
}

.plan-badge {
  padding: 0.25rem 0.625rem;
  border-radius: 0.375rem;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: capitalize;
}

.plan-basic {
  background: rgba(59, 130, 246, 0.1);
  color: #60a5fa;
}

.plan-standard {
  background: rgba(168, 85, 247, 0.1);
  color: #c084fc;
}

.plan-pro {
  background: rgba(236, 72, 153, 0.1);
  color: #f472b6;
}

.loading-state, .empty-state {
  text-align: center;
  padding: 3rem 0;
  color: #71717a;
}

.spinner {
  width: 2rem;
  height: 2rem;
  border: 3px solid rgba(255, 255, 255, 0.1);
  border-top-color: #6366f1;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto 1rem;
}

.toast {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: #22c55e;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  font-size: 0.75rem;
  font-weight: 600;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
  z-index: 10;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.fade-enter-from, .fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

@media (max-width: 768px) {
  .list-header {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .controls {
    width: 100%;
    flex-direction: column;
  }
  
  .control-select {
    width: 100%;
  }

  table, thead, tbody, th, td, tr {
    display: block;
  }

  thead tr {
    position: absolute;
    top: -9999px;
    left: -9999px;
  }

  tr {
    margin-bottom: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 1rem;
    padding: 0.5rem;
    background: rgba(255, 255, 255, 0.02);
  }

  td {
    border: none;
    position: relative;
    padding-left: 45%;
    text-align: right;
    min-height: 2.5rem;
    display: flex;
    align-items: center;
    justify-content: flex-end;
  }

  td:before {
    position: absolute;
    left: 1rem;
    width: 40%;
    padding-right: 10px;
    white-space: nowrap;
    content: attr(data-label);
    text-align: left;
    font-weight: 600;
    color: #71717a;
    font-size: 0.75rem;
    text-transform: uppercase;
  }

  .email-wrapper {
    justify-content: flex-end;
  }
}
</style>
