import { describe, it, expect, vi } from 'vitest';
import axios from 'axios';
import { ApiClient } from "@/lib/api";

vi.mock('axios');

describe("Test ApiClient", () => {
    it('getAllLaunchpadNames gets data correctly', async () => {
        const mockData = { id: 1, name: 'Mock Data' };
        const mockGet = vi.fn().mockResolvedValue({ data: mockData });
    
        axios.create = vi.fn().mockReturnValue({
          get: mockGet,
        });
    
        const apiClient = new ApiClient();
        const data = await apiClient.getAllLaunchpadNames();
    
        expect(axios.create).toHaveBeenCalled();
        expect(mockGet).toHaveBeenCalledWith('get_all_launchpad_names');
        expect(data).toEqual(mockData);
    });

    it('getAllLaunchpadNames handles error', async () => {
        const mockError = new Error('Network Error');
        const mockGet = vi.fn().mockRejectedValue(mockError);

        axios.create = vi.fn().mockReturnValue({
        get: mockGet,
        });

        const apiClient = new ApiClient();

        await expect(apiClient.getAllLaunchpadNames()).rejects.toThrow('Network Error');
        expect(axios.create).toHaveBeenCalled();
        expect(mockGet).toHaveBeenCalledWith('get_all_launchpad_names');
    });
    it('getAllUniqueLaunchYears gets data correctly', async () => {
        const mockData = { id: 1, name: 'Mock Data' };
        const mockGet = vi.fn().mockResolvedValue({ data: mockData });

        axios.create = vi.fn().mockReturnValue({
            get: mockGet,
        });

        const apiClient = new ApiClient();
        const data = await apiClient.getAllUniqueLaunchYears();

        expect(axios.create).toHaveBeenCalled();
        expect(mockGet).toHaveBeenCalledWith('get_all_launch_years');
        expect(data).toEqual(mockData);
    });

    it('getAllUniqueLaunchYears handles error', async () => {
        const mockError = new Error('Network Error');
        const mockGet = vi.fn().mockRejectedValue(mockError);

        axios.create = vi.fn().mockReturnValue({
        get: mockGet,
        });

        const apiClient = new ApiClient();

        await expect(apiClient.getAllUniqueLaunchYears()).rejects.toThrow('Network Error');
        expect(axios.create).toHaveBeenCalled();
        expect(mockGet).toHaveBeenCalledWith('get_all_launch_years');
    });
    it('getAllLaunchesInYear gets data correctly', async () => {
        const mockData = { id: 1, name: 'Mock Data' };
        const mockGet = vi.fn().mockResolvedValue({ data: mockData });

        axios.create = vi.fn().mockReturnValue({
            get: mockGet,
        });

        const apiClient = new ApiClient();
        const data = await apiClient.getAllLaunchesInYear("2001");

        expect(axios.create).toHaveBeenCalled();
        expect(mockGet).toHaveBeenCalledWith('/2001/get_all_launches_in_year');
        expect(data).toEqual(mockData);
    });

    it('getAllLaunchesInYear handles error', async () => {
        const mockError = new Error('Network Error');
        const mockGet = vi.fn().mockRejectedValue(mockError);

        axios.create = vi.fn().mockReturnValue({
        get: mockGet,
        });

        const apiClient = new ApiClient();

        await expect(apiClient.getAllLaunchesInYear("2001")).rejects.toThrow('Network Error');
        expect(axios.create).toHaveBeenCalled();
        expect(mockGet).toHaveBeenCalledWith('/2001/get_all_launches_in_year');
    });

    it('getLaunchpadWithLaunches gets data correctly', async () => {
        const mockData = { id: 1, name: 'Mock Data' };
        const mockGet = vi.fn().mockResolvedValue({ data: mockData });

        axios.create = vi.fn().mockReturnValue({
            get: mockGet,
        });

        const apiClient = new ApiClient();
        const data = await apiClient.getLaunchpadWithLaunches("testid", "testname");

        expect(axios.create).toHaveBeenCalled();
        expect(mockGet).toHaveBeenCalledWith('testid/testname/get_launchpad_with_launches');
        expect(data).toEqual(mockData);
    });

    it('getLaunchpadWithLaunches handles error', async () => {
        const mockError = new Error('Network Error');
        const mockGet = vi.fn().mockRejectedValue(mockError);

        axios.create = vi.fn().mockReturnValue({
        get: mockGet,
        });

        const apiClient = new ApiClient();

        await expect(apiClient.getLaunchpadWithLaunches("testid", "testname")).rejects.toThrow('Network Error');
        expect(axios.create).toHaveBeenCalled();
        expect(mockGet).toHaveBeenCalledWith('testid/testname/get_launchpad_with_launches');
    });
})
