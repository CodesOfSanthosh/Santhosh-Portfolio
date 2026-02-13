# 🚀 Vercel Deployment Guide for Django Portfolio

## Prerequisites
- GitHub account
- Vercel account (sign up at https://vercel.com)
- Git installed on your machine

## Step-by-Step Deployment Instructions

### 1️⃣ Prepare Your Repository

First, make sure all your changes are committed to Git:

```bash
git add .
git commit -m "Add Vercel deployment configuration"
git push origin main
```

### 2️⃣ Set Up Vercel Account

1. Go to https://vercel.com
2. Click "Sign Up" and choose "Continue with GitHub"
3. Authorize Vercel to access your GitHub account

### 3️⃣ Import Your Project

1. Click "Add New..." → "Project"
2. Import your GitHub repository
3. Vercel will auto-detect it as a Python project

### 4️⃣ Configure Environment Variables

In the Vercel project settings, add these environment variables:

**Required:**
- `SECRET_KEY` = (generate a new secret key)
- `DEBUG` = `False`
- `ALLOWED_HOSTS` = `.vercel.app`

**Optional (if using Cloudinary):**
- `CLOUDINARY_CLOUD_NAME` = your-cloud-name
- `CLOUDINARY_API_KEY` = your-api-key
- `CLOUDINARY_API_SECRET` = your-api-secret

**Database (if using PostgreSQL):**
- `DATABASE_URL` = your-postgres-connection-string

### 5️⃣ Deploy

1. Click "Deploy"
2. Wait for the build to complete (2-5 minutes)
3. Your site will be live at `https://your-project.vercel.app`

## 🔧 Important Notes

### Database Considerations
- **SQLite won't work on Vercel** (serverless environment)
- Use **Vercel Postgres** (free tier available) or **Neon** (free PostgreSQL)
- Alternative: Use **Supabase** or **PlanetScale**

### Static Files
- Static files are served via WhiteNoise
- Run `python manage.py collectstatic` locally first to test

### Media Files
- Use **Cloudinary** for media file storage (already configured)
- Vercel serverless functions are stateless (no persistent file storage)

## 🗄️ Setting Up Vercel Postgres (Free)

1. In your Vercel project dashboard, go to "Storage"
2. Click "Create Database" → "Postgres"
3. Copy the `DATABASE_URL` environment variable
4. Add it to your Vercel project environment variables
5. Redeploy your project

## 🔄 Automatic Deployments

Every time you push to your `main` branch, Vercel will automatically:
- Build your project
- Run tests (if configured)
- Deploy the new version

## 🐛 Troubleshooting

### Build Fails
- Check the build logs in Vercel dashboard
- Ensure all dependencies are in `requirements.txt`
- Verify Python version compatibility

### 500 Internal Server Error
- Check environment variables are set correctly
- Ensure `DEBUG=False` in production
- Check Vercel function logs

### Static Files Not Loading
- Run `python manage.py collectstatic` locally
- Check `STATIC_ROOT` and `STATIC_URL` in settings.py
- Verify WhiteNoise is in `MIDDLEWARE`

## 📱 Custom Domain (Optional)

1. Go to your Vercel project settings
2. Click "Domains"
3. Add your custom domain
4. Update DNS records as instructed

## 🎉 Your Site is Live!

Once deployed, your portfolio will be accessible 24/7 at:
`https://your-project-name.vercel.app`

---

**Need help?** Check Vercel docs: https://vercel.com/docs
