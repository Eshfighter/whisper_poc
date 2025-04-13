import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import FileUpload from './FileUpload';

test('renders FileUpload component', () => {
  render(<FileUpload />);
  const uploadButton = screen.getByText(/upload/i);
  expect(uploadButton).toBeInTheDocument();
}); 