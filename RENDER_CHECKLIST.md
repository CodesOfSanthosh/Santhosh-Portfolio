# 🚀 Render Deployment Quick Checklist

## Before You Start
- ✅ GitHub repo: https://github.com/CodesOfSanthosh/portfolio
- ✅ Code is pushed to GitHub
- ✅ Have a secret key ready (get from https://djecrety.ir/)

---

## Deployment Steps (10 Minutes)

### 1️⃣ Sign Up to Render
- [ ] Go to https://render.com
- [ ] Click "Get Started for Free"
- [ ] Sign up with GitHub
- [ ] Authorize Render

### 2️⃣ Create Web Service
- [ ] Click "New +" button (top right)
- [ ] Select "Web Service"
- [ ] Search for "portfolio"
- [ ] Click "Connect" on CodesOfSanthosh/portfolio

### 3️⃣ Configure Service
Fill in these fields:

**Name:**
```
santhosh-portfolio
```

**Region:**
```
Singapore (or closest to you)
```

**Branch:**
```
main
```

**Build Command:**
```
pip install -r requirements.txt
```

**Start Command:**
```
gunicorn portfolio.wsgi:application
```

### 4️⃣ Add Environment Variables
Click "Add Environment Variable" for each:

**Variable 1:**
- Key: `SECRET_KEY`
- Value: [Get from https://djecrety.ir/]

**Variable 2:**
- Key: `DEBUG`
- Value: `False`

**Variable 3:**
- Key: `ALLOWED_HOSTS`
- Value: `.onrender.com`

### 5️⃣ Select Plan
- [ ] Choose "Free" plan
- [ ] Enable "Auto-Deploy"

### 6️⃣ Deploy
- [ ] Click "Create Web Service"
- [ ] Wait 5-10 minutes
- [ ] Watch the logs

### 7️⃣ Post-Deployment (In Render Shell)
- [ ] Click "Shell" tab
- [ ] Run: `python manage.py migrate`
- [ ] Run: `python manage.py createsuperuser`
- [ ] Run: `python manage.py collectstatic --noinput`

### 8️⃣ Test Your Site
- [ ] Visit: https://santhosh-portfolio.onrender.com
- [ ] Test navigation
- [ ] Test mobile menu
- [ ] Test contact form
- [ ] Access admin: /admin

---

## 🎉 You're Live!

**Your Portfolio:** https://santhosh-portfolio.onrender.com
**Admin Panel:** https://santhosh-portfolio.onrender.com/admin

---

## 🔄 To Update Later

```bash
git add .
git commit -m "Update message"
git push origin main
```

Render auto-deploys in 3-5 minutes!

---

## 📚 Full Guide
See `RENDER_DEPLOYMENT_DETAILED.md` for complete instructions.
