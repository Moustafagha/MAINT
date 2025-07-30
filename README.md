# Predictive Failure Monitor - AI Dashboard

A real-time machine health monitoring dashboard with AI-powered failure predictions. This React application provides a comprehensive view of machine sensor data and predictive analytics.

## Features

- **Real-time Monitoring**: Live sensor data display (temperature, vibration, pressure)
- **AI-Powered Predictions**: Machine learning-based failure probability assessment
- **Historical Trends**: Interactive charts showing sensor data over time
- **Alert System**: Visual indicators for different alert levels (normal, warning, critical)
- **Auto-refresh**: Data updates every 5 seconds
- **Responsive Design**: Works on desktop and mobile devices

## Tech Stack

- **Frontend**: React 19, Vite
- **UI Components**: Radix UI, Tailwind CSS
- **Charts**: Recharts
- **Icons**: Lucide React
- **Styling**: Tailwind CSS with custom design system

## Project Structure

```
├── src/
│   ├── components/ui/     # UI components (Card, Badge, etc.)
│   ├── lib/              # Utility functions
│   ├── App.jsx           # Main application component
│   ├── main.jsx          # Application entry point
│   └── index.css         # Global styles and Tailwind imports
├── public/               # Static assets
├── package.json          # Dependencies and scripts
├── vite.config.js        # Vite configuration
├── tailwind.config.js    # Tailwind CSS configuration
└── vercel.json          # Vercel deployment configuration
```

## Getting Started

### Prerequisites

- Node.js 18+ 
- npm or pnpm

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd predictive-frontend
```

2. Install dependencies:
```bash
npm install --legacy-peer-deps
```

3. Start the development server:
```bash
npm run dev
```

4. Open [http://localhost:5173](http://localhost:5173) in your browser.

### Building for Production

```bash
npm run build
```

The built files will be in the `dist/` directory.

## Deployment

### Deploy to Vercel

1. Install Vercel CLI:
```bash
npm i -g vercel
```

2. Deploy to Vercel:
```bash
vercel
```

Or connect your GitHub repository to Vercel for automatic deployments.

### Environment Variables

The application uses the following environment variables:

- `NODE_ENV`: Set to 'production' for deployment
- API endpoints are automatically configured based on the environment

### API Configuration

The application expects a backend API with the following endpoints:

- `GET /api/machine-status` - Current machine status and sensor data
- `GET /api/historical-data?limit=20` - Historical sensor data

## API Response Format

### Machine Status Endpoint

```json
{
  "success": true,
  "data": {
    "machine_id": "MACHINE_001",
    "machine_name": "Production Line 1",
    "current_status": "operational",
    "alert_level": "normal",
    "failure_probability": 15.5,
    "sensor_readings": {
      "temperature": 65.2,
      "vibration": 0.15,
      "pressure": 120.5
    },
    "last_updated": 1640995200
  }
}
```

### Historical Data Endpoint

```json
{
  "success": true,
  "data": [
    {
      "temperature": 65.2,
      "vibration": 0.15,
      "pressure": 120.5,
      "failure_probability": 15.5,
      "timestamp": 1640995200
    }
  ]
}
```

## Development

### Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

### Code Structure

The application follows a component-based architecture:

- **App.jsx**: Main application component with state management
- **UI Components**: Reusable components in `src/components/ui/`
- **Utils**: Helper functions in `src/lib/utils.js`

## Troubleshooting

### Common Issues

1. **Build Errors**: Ensure all dependencies are installed with `--legacy-peer-deps`
2. **API Connection**: Check that the backend API is running and accessible
3. **Styling Issues**: Verify Tailwind CSS is properly configured

### Performance Optimization

- The application uses React 19 with automatic batching
- Charts are optimized with Recharts
- CSS is purged in production builds

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support and questions, please open an issue in the repository.

