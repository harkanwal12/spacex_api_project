import { describe, it, expect, vi } from 'vitest';
import axios from 'axios';
import { ApiClient } from "@/lib/api";

vi.mock('axios');

describe("Test ApiClient", () => {
    it('getAllLaunches gets data correctly', async () => {
        const mockData = { id: 1, name: 'Mock Data' };
        const mockGet = vi.fn().mockResolvedValue({ data: mockData });
    
        axios.create = vi.fn().mockReturnValue({
          get: mockGet,
        });
    
        const apiClient = new ApiClient();
        const data = await apiClient.getAllLaunches();
    
        expect(axios.create).toHaveBeenCalled();
        expect(mockGet).toHaveBeenCalledWith('get_all_launches');
        expect(data).toEqual(mockData);
    });

    it('getAllLaunches handles error', async () => {
        const mockError = new Error('Network Error');
        const mockGet = vi.fn().mockRejectedValue(mockError);

        axios.create = vi.fn().mockReturnValue({
        get: mockGet,
        });

        const apiClient = new ApiClient();

        await expect(apiClient.getAllLaunches()).rejects.toThrow('Network Error');
        expect(axios.create).toHaveBeenCalled();
        expect(mockGet).toHaveBeenCalledWith('get_all_launches');
    });

    it('getAllLaunchpadsWithLaunches gets data correctly', async () => {
        const mockData = { id: 1, name: 'Mock Data' };
        const mockGet = vi.fn().mockResolvedValue({ data: mockData });

        axios.create = vi.fn().mockReturnValue({
            get: mockGet,
        });

        const apiClient = new ApiClient();
        const data = await apiClient.getAllLaunchpadsWithLaunches();

        expect(axios.create).toHaveBeenCalled();
        expect(mockGet).toHaveBeenCalledWith('get_all_launchpads_with_launches');
        expect(data).toEqual(mockData);
    });

    it('getAllLaunchpadsWithLaunches handles error', async () => {
        const mockError = new Error('Network Error');
        const mockGet = vi.fn().mockRejectedValue(mockError);

        axios.create = vi.fn().mockReturnValue({
        get: mockGet,
        });

        const apiClient = new ApiClient();

        await expect(apiClient.getAllLaunchpadsWithLaunches()).rejects.toThrow('Network Error');
        expect(axios.create).toHaveBeenCalled();
        expect(mockGet).toHaveBeenCalledWith('get_all_launchpads_with_launches');
    });
})