import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import App from '../App.tsx';

describe('App', () => {
  it('renders the app correctly', () => {
    render(<App />);
    expect(screen.getByText(/Welcome to the unofficial/i)).toBeInTheDocument();
  });
});