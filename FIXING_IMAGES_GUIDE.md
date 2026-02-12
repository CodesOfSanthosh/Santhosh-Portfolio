# Fixing Images and Media Files on Render

## ⚠️ The Problem

Render's free tier has **ephemeral storage** - any files uploaded through Django admin (images, PDFs) are deleted when the service redeploys or restarts.

## ✅ Solutions Implemented

### 1. Resume Download - FIXED ✅
- **Problem:** Resume was in `/media` folder (gets deleted)
- **Solution:** Moved to `/static` folder (persists across deployments)
- **Status:** Resume download now works permanently!

---

### 2. Project Images - Two Options

#### **Option A: Use Image URLs (Recommended)**

Instead of uploading images, use external URLs:

**Step 1: Upload images to GitHub**
1. Create a folder in your repo: `project_images/`
2. Add your project screenshots there
3. Commit and push to GitHub

**Step 2: Get the raw URL**
Format: `https://raw.githubusercontent.com/CodesOfSanthosh/portfolio/main/project_images/YOUR_IMAGE.png`

**Step 3: In Django Admin**
- When adding a project, **leave the image field empty**
- We'll update the template to use URLs instead

---

#### **Option B: Use Cloudinary (Free Cloud Storage)**

**Step 1: Sign up for Cloudinary**
1. Go to: https://cloudinary.com
2. Sign up for free account
3. Get your cloud name, API key, and API secret

**Step 2: Install Cloudinary**
Add to `requirements.txt`:
```
cloudinary
django-cloudinary-storage
```

**Step 3: Update settings.py**
```python
INSTALLED_APPS = [
    ...
    'cloudinary_storage',
    'cloudinary',
    ...
]

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'your_cloud_name',
    'API_KEY': 'your_api_key',
    'API_SECRET': 'your_api_secret',
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

---

## 🎯 Quick Fix for Now

### For Project Images:

**Option 1: Use Placeholder Images**
In Django admin, when adding projects, use these placeholder URLs:
```
https://via.placeholder.com/600x400/2563eb/ffffff?text=E-commerce+Platform
https://via.placeholder.com/600x400/2563eb/ffffff?text=Job+Portal
https://via.placeholder.com/600x400/2563eb/ffffff?text=Portfolio+Website
```

**Option 2: Use Your Actual Project Screenshots**
1. Take screenshots of your projects
2. Upload to: https://imgur.com (free, no account needed)
3. Copy the direct image link
4. Use that URL in Django admin

---

## 📝 Updated Instructions for Adding Projects

### In Django Admin:

1. **Title:** `E-commerce Platform`
2. **Description:** Your project description
3. **Tech Stack:** `Django, React, MySQL`
4. **GitHub Link:** `https://github.com/CodesOfSanthosh/ecommerce`
5. **Live Link:** (if you have one)
6. **Image:** **LEAVE EMPTY** (or use Imgur/placeholder URL if the model accepts URLs)

---

## 🔄 Current Status

### ✅ Working:
- Resume download (moved to static files)
- Media URL configuration updated
- Site is live and functional

### ⚠️ Needs Attention:
- Project images (use external URLs or Cloudinary)
- Any other uploaded files through admin

---

## 💡 Recommended Workflow

**For permanent file storage on Render free tier:**

1. **Static files** (CSS, JS, fonts, resume) → Store in `/static` folder ✅
2. **Project images** → Use external URLs (GitHub, Imgur, Cloudinary)
3. **User uploads** → Use Cloudinary or AWS S3

---

## 🚀 Next Steps

1. **Resume:** Already fixed! ✅
2. **Project Images:** 
   - Upload screenshots to Imgur
   - Use the direct links when adding projects in admin
3. **Test:** Visit your portfolio and verify everything works

---

## 📸 How to Get Image URLs

### Method 1: Imgur (Easiest)
1. Go to https://imgur.com
2. Click "New post"
3. Upload your image
4. Right-click on image → "Copy image address"
5. Use that URL

### Method 2: GitHub
1. Add images to your repo in `project_images/` folder
2. Commit and push
3. Go to GitHub, click on the image
4. Click "Raw" button
5. Copy the URL

### Method 3: Placeholder (Temporary)
Use: `https://via.placeholder.com/600x400/2563eb/ffffff?text=Project+Name`

---

## ✅ Summary

- ✅ Resume download: **FIXED** (now uses static files)
- ⚠️ Project images: **Use external URLs** (Imgur, GitHub, or Cloudinary)
- ✅ Site is live: https://santhosh-portfolio-059h.onrender.com

**Your portfolio is functional! Just use image URLs for projects instead of uploading files.** 🎉
