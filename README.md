# Predictive Failure Monitor - AI Dashboard

A real-time machine health monitoring dashboard with AI-powered failure prediction capabilities.

## Features

- **Real-time Monitoring**: Live sensor data display (temperature, vibration, pressure)
- **AI Predictions**: Machine learning-based failure probability assessment
- **Historical Trends**: Interactive charts showing sensor data over time
- **Alert System**: Visual indicators for normal, warning, and critical states
- **Auto-refresh**: Data updates every 5 seconds automatically

## Tech Stack

- **Frontend**: React 18 + Vite
- **UI Components**: Radix UI + Tailwind CSS
- **Charts**: Recharts
- **Icons**: Lucide React
- **Deployment**: Vercel

## Project Structure

```
├── src/
│   ├── components/ui/     # UI components (Card, Badge, etc.)
│   ├── lib/              # Utility functions
│   ├── App.jsx           # Main application component
│   ├── main.jsx          # Application entry point
│   ├── App.css           # Application styles
│   └── index.css         # Global styles
├── public/               # Static assets
├── index.html            # HTML template
├── package.json          # Dependencies and scripts
├── vite.config.js        # Vite configuration
└── vercel.json          # Vercel deployment config
```

## Local Development

1. **Install dependencies**:
   ```bash
   npm install
   ```

2. **Start development server**:
   ```bash
   npm run dev
   ```

3. **Build for production**:
   ```bash
   npm run build
   ```

## Deployment to Vercel

### Automatic Deployment

1. Connect your GitHub repository to Vercel
2. Vercel will automatically detect the Vite framework
3. The build settings are configured in `vercel.json`

### Manual Deployment

1. **Install Vercel CLI**:
   ```bash
   npm i -g vercel
   ```

2. **Deploy**:
   ```bash
   vercel
   ```

### Environment Variables

The application uses the following environment variables:

- `NODE_ENV`: Set to 'production' for deployment
- API endpoints are automatically configured for both development and production

## API Integration

The dashboard expects a backend API with the following endpoints:

- `GET /api/machine-status` - Current machine status and sensor readings
- `GET /api/historical-data?limit=20` - Historical sensor data

### Expected API Response Format

```json
{
  "success": true,
  "data": {
    "machine_id": "MACHINE_001",
    "machine_name": "Production Line A",
    "current_status": "operational",
    "alert_level": "normal",
    "sensor_readings": {
      "temperature": 45.2,
      "vibration": 0.15,
      "pressure": 120.5
    },
    "failure_probability": 12.5,
    "last_updated": 1640995200
  }
}
```

## Troubleshooting

### Common Issues

1. **Build Errors**: Ensure all dependencies are installed with `npm install`
2. **API Connection**: Check that the backend API is running and accessible
3. **Component Errors**: Verify that all UI components are properly imported

### Development vs Production

- **Development**: API calls go to `http://localhost:5000/api`
- **Production**: API calls go to `/api` (relative path)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - see LICENSE file for details

