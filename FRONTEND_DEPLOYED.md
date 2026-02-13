# 🎉 FRONTEND DEPLOYED TO GITHUB!

## ✅ What's Done:

Your static portfolio has been pushed to:
**https://github.com/CodesOfSanthosh/Santhosh-Portfolio**

---

## 🚀 NEXT STEP: ENABLE GITHUB PAGES

### Manual Setup (Do this now):

1. **Go to your repository:**
   - https://github.com/CodesOfSanthosh/Santhosh-Portfolio

2. **Click "Settings" tab** (top right)

3. **Click "Pages"** (left sidebar)

4. **Under "Source":**
   - Branch: Select **"main"**
   - Folder: Select **"/ (root)"**
   - Click **"Save"**

5. **Wait 2-3 minutes**

6. **Refresh the page**
   - You'll see: "Your site is published at https://codesofsanthosh.github.io/Santhosh-Portfolio/"

7. **Visit your site:**
   - https://codesofsanthosh.github.io/Santhosh-Portfolio/

✅ **Frontend is LIVE!**

---

## 📝 UPDATE API URL

Now that you know your frontend URL, update the backend CORS:

1. Open: `c:\Users\gunap\OneDrive\Desktop\Portfolio\portfolio\settings.py`

2. Find `CORS_ALLOWED_ORIGINS` (line ~145)

3. Update to:
   ```python
   CORS_ALLOWED_ORIGINS = [
       "https://codesofsanthosh.github.io",
   ]
   ```

4. Save the file

---

## 🔄 NEXT: DEPLOY BACKEND TO RENDER

Follow these steps:

### 1. Commit Backend Changes

```powershell
cd c:\Users\gunap\OneDrive\Desktop\Portfolio
git add .
git commit -m "Add REST API for contact form"
git push origin main
```

### 2. Deploy to Render

1. Go to: https://dashboard.render.com
2. Sign up/Login with GitHub
3. Click **"New +"** → **"Web Service"**
4. Connect your **Portfolio** repository
5. Configure:
   - **Name:** `portfolio-backend`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn portfolio.wsgi:application`
   - **Environment Variables:**
     - `SECRET_KEY` = (generate new)
     - `DEBUG` = `False`
     - `ALLOWED_HOSTS` = `.onrender.com`

6. Click **"Create Web Service"**
7. Wait 5-10 minutes for deployment
8. Copy your backend URL: `https://portfolio-backend-xxxx.onrender.com`

### 3. Update Frontend with Backend URL

1. Open: `c:\Users\gunap\OneDrive\Desktop\Portfolio\portfolio-frontend\index.html`
2. Find line ~360: `const API_URL`
3. Update to:
   ```javascript
   const API_URL = 'https://portfolio-backend-xxxx.onrender.com/api/contact/';
   ```
4. Save and push:
   ```powershell
   cd c:\Users\gunap\OneDrive\Desktop\Portfolio\portfolio-frontend
   git add index.html
   git commit -m "Update API URL"
   git push
   ```

---

## ✅ CHECKLIST

- [x] Frontend code pushed to GitHub
- [ ] GitHub Pages enabled (do this now!)
- [ ] Backend CORS updated
- [ ] Backend pushed to GitHub
- [ ] Backend deployed to Render
- [ ] Frontend API URL updated
- [ ] Contact form tested

---

**Your frontend is deployed! Now enable GitHub Pages and deploy the backend!** 🚀
