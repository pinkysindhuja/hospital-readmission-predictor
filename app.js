require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
const session=require('express-session');
const MongoStore=require('connect-mongo');
const bodyParser = require('body-parser');
const patientRoutes = require('./routes/patientRoutes');
const analyticsRoutes = require('./routes/inde.js');
const path = require('path');


const store=new MongoStore({
mongoUrl:process.env.MONGO_URI,
Crypto:{
secret:"mysupersetcode",
},
touchAfter:24*3600,
  });


  store.on("errror",()=>{
    console.log("error in mongostore",err);
  });
const app = express();



app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'));


// Connect to MongoDB
mongoose.connect(process.env.MONGO_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
}).then(() => console.log('MongoDB Connected'))
  .catch(err => console.error('MongoDB connection error:', err));



 

// Set view engine
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Middlewares
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

// Routes
app.get('/', (req, res) => {
  res.render('home');
});
app.use('/patients', patientRoutes);


app.use('/', analyticsRoutes);



app.get('/about', (req, res) => {
  res.render('about');
});
app.get('/faq', (req, res) => {
  res.render('faq');
});
app.get('/contact', (req, res) => {
  res.render('contact');
});

app.post('/contact', async(req, res) => {
  console.log('Contact form submitted:', req.body);
  // You can later save this info to DB or send email
  res.send('Thank you for contacting us!');
});


app.get('/analytics', (req, res) => {
  res.render('analytics');
});

// 404 Handler
app.use((req, res) => {
  res.status(404).send('Page Not Found');
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT,"0.0.0.0", () => {
  console.log(`Server running on port ${PORT}`);
});
