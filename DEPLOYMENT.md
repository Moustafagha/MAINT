# Vercel Deployment Guide

## Quick Deploy to Vercel

### Option 1: Deploy with Vercel CLI

1. **Install Vercel CLI**:
   ```bash
   npm i -g vercel
   ```

2. **Login to Vercel**:
   ```bash
   vercel login
   ```

3. **Deploy**:
   ```bash
   vercel
   ```

4. **Follow the prompts**:
   - Link to existing project or create new
   - Confirm deployment settings
   - Wait for build to complete

### Option 2: Deploy via GitHub

1. **Push your code to GitHub**

2. **Connect to Vercel**:
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project"
   - Import your GitHub repository
   - Vercel will auto-detect Vite settings

3. **Deploy**:
   - Click "Deploy"
   - Vercel will build and deploy automatically

## Build Configuration

The project is configured for Vercel with:

- **Framework**: Vite
- **Build Command**: `npm run build`
- **Output Directory**: `dist`
- **Node Version**: 18.x (auto-detected)

## Environment Variables

No environment variables are required for basic deployment. The app automatically detects production vs development mode.

## API Configuration

The app expects a backend API. For production:

1. **Deploy your backend** to a service like:
   - Railway
   - Render
   - Heroku
   - DigitalOcean

2. **Update API URL** in the frontend if needed:
   - Edit `src/App.jsx` line 8
   - Change the API_BASE_URL for production

## Troubleshooting

### Build Errors

1. **Dependency Issues**:
   ```bash
   npm install --legacy-peer-deps
   ```

2. **Node Version**:
   - Ensure Node.js 18+ is used
   - Vercel auto-detects this

### Runtime Errors

1. **API Connection**:
   - Check browser console for CORS errors
   - Ensure backend is deployed and accessible

2. **Component Errors**:
   - Verify all imports are correct
   - Check that all UI components exist

## Custom Domain

1. **Add Domain in Vercel Dashboard**
2. **Configure DNS** as instructed
3. **SSL Certificate** is auto-provisioned

## Monitoring

- **Vercel Analytics**: Available in dashboard
- **Function Logs**: Check Vercel dashboard for errors
- **Performance**: Built-in performance monitoring

## Updates

To update your deployment:

1. **Push changes to GitHub**
2. **Vercel auto-deploys** on push to main branch
3. **Preview deployments** for pull requests

## Support

- **Vercel Documentation**: [vercel.com/docs](https://vercel.com/docs)
- **Vite Documentation**: [vitejs.dev](https://vitejs.dev)
- **React Documentation**: [react.dev](https://react.dev)

