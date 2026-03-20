export interface WaitingListEntry {
  id: number;
  name: string;
  email: string;
  phone: string;
  plan_type: 'basic' | 'standard' | 'pro';
  created_at: string;
}

const API_BASE_URL = import.meta.env.VITE_API_URL || '/api/v1/waiting-list';

export class WaitingListService {
  static async getGeneralList(): Promise<WaitingListEntry[]> {
    const response = await fetch(`${API_BASE_URL}/general`);
    if (!response.ok) throw new Error('Failed to fetch general waiting list');
    return response.json();
  }

  static async getExclusiveList(): Promise<WaitingListEntry[]> {
    const response = await fetch(`${API_BASE_URL}/exclusive`);
    if (!response.ok) throw new Error('Failed to fetch exclusive waiting list');
    return response.json();
  }
}
