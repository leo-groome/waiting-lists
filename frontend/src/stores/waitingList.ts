import { defineStore } from 'pinia';
import { WaitingListService, type WaitingListEntry } from '../services/WaitingListService';

export const useWaitingListStore = defineStore('waitingList', {
  state: () => ({
    generalList: [] as WaitingListEntry[],
    exclusiveList: [] as WaitingListEntry[],
    loading: false,
    error: null as string | null,
  }),
  
  getters: {
    sortedGeneralList: (state) => {
      return [...state.generalList].sort((a, b) => 
        new Date(b.created_at).getTime() - new Date(a.created_at).getTime()
      );
    },
    sortedExclusiveList: (state) => {
      return [...state.exclusiveList].sort((a, b) => 
        new Date(b.created_at).getTime() - new Date(a.created_at).getTime()
      );
    }
  },

  actions: {
    async fetchAllLists() {
      this.loading = true;
      this.error = null;
      try {
        const [general, exclusive] = await Promise.all([
          WaitingListService.getGeneralList(),
          WaitingListService.getExclusiveList(),
        ]);
        this.generalList = general;
        this.exclusiveList = exclusive;
      } catch (err: any) {
        this.error = err.message || 'An error occurred while fetching lists';
      } finally {
        this.loading = false;
      }
    }
  }
});
