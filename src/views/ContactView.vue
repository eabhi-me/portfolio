<template>
  <div class="contact">
    <!-- Hero Section -->
    <section class="contact-hero">
      <div class="container">
        <div class="hero-content">
          <h1 class="section-title">Get In Touch</h1>
          <p class="hero-subtitle">
            Let's connect and discuss opportunities, collaborations, or just have a great
            conversation about technology
          </p>
        </div>
      </div>
    </section>

    <!-- Contact Content -->
    <section class="contact-content">
      <div class="container">
        <div class="contact-grid">
          <!-- Contact Information -->
          <div class="contact-info">
            <h2>Let's Connect</h2>
            <p class="contact-description">
              I'm always excited to connect with fellow developers, potential collaborators, and
              anyone interested in technology. Whether you have a project in mind, want to discuss
              opportunities, or just want to chat about the latest in tech, I'd love to hear from
              you!
            </p>

            <div class="contact-methods">
              <div class="contact-method">
                <div class="method-icon">📧</div>
                <div class="method-content">
                  <h3>Email</h3>
                  <a href="mailto:eabhi.me@gmail.com" class="contact-link">eabhi.me@gmail.com</a>
                  <span class="method-note"> Best for detailed discussions</span>
                </div>
              </div>

              <div class="contact-method">
                <div class="method-icon">💼</div>
                <div class="method-content">
                  <h3>LinkedIn</h3>
                  <a
                    href="https://linkedin.com/in/eabhi-me/"
                    target="_blank"
                    rel="noopener noreferrer"
                    class="contact-link"
                    >linkedin.com/in/eabhi-me/</a
                  >
                  <span class="method-note"> Professional networking</span>
                </div>
              </div>

              <div class="contact-method">
                <div class="method-icon">🐙</div>
                <div class="method-content">
                  <h3>GitHub</h3>
                  <a
                    href="https://github.com/eabhi-me"
                    target="_blank"
                    rel="noopener noreferrer"
                    class="contact-link"
                    >github.com/eabhi-me</a
                  >
                  <span class="method-note"> Check out my code</span>
                </div>
              </div>

              <!-- <div class="contact-method">
                <div class="method-icon">🌐</div>
                <div class="method-content">
                  <h3>Website</h3>
                  <a
                    href="https://brahamadevi.in"
                    target="_blank"
                    rel="noopener noreferrer"
                    class="contact-link"
                    >brahamadevi.in</a
                  >
                  <span class="method-note">My personal projects</span>
                </div>
              </div> -->
            </div>

            <div class="availability">
              <h3>Availability</h3>
              <div class="availability-status">
                <div class="status-indicator available"></div>
                <span>Available for new opportunities</span>
              </div>
              <p class="availability-note">
                Currently seeking internship opportunities and open to freelance projects
              </p>
            </div>
          </div>

          <!-- Contact Form -->
          <div class="contact-form-container">
            <form @submit.prevent="submitForm" class="contact-form">
              <h2>Send a Message</h2>

              <div class="form-group">
                <label for="name">Your Name</label>
                <input
                  type="text"
                  id="name"
                  v-model="form.name"
                  required
                  placeholder="Enter your full name"
                  class="form-input"
                />
              </div>

              <div class="form-group">
                <label for="email">Email Address</label>
                <input
                  type="email"
                  id="email"
                  v-model="form.email"
                  required
                  placeholder="your.email@example.com"
                  class="form-input"
                />
              </div>

              <div class="form-group">
                <label for="subject">Subject</label>
                <select id="subject" v-model="form.subject" required class="form-select">
                  <option value="">Select a subject</option>
                  <option value="collaboration">Project Collaboration</option>
                  <option value="opportunity">Job Opportunity</option>
                  <option value="freelance">Freelance Project</option>
                  <option value="mentorship">Mentorship</option>
                  <option value="general">General Inquiry</option>
                  <option value="other">Other</option>
                </select>
              </div>

              <div class="form-group">
                <label for="message">Message</label>
                <textarea
                  id="message"
                  v-model="form.message"
                  required
                  rows="6"
                  placeholder="Tell me about your project or inquiry..."
                  class="form-textarea"
                ></textarea>
              </div>

              <div class="form-group">
                <label class="checkbox-label">
                  <input type="checkbox" v-model="form.newsletter" class="checkbox-input" />
                  <span class="checkbox-custom"></span>
                  I'd like to receive updates about your latest projects
                </label>
              </div>

              <button
                type="submit"
                class="submit-btn"
                :disabled="isSubmitting"
                :class="{ submitting: isSubmitting }"
              >
                <span v-if="!isSubmitting">Send Message</span>
                <span v-else>Sending...</span>
              </button>

              <div v-if="submitStatus" class="submit-status" :class="submitStatus.type">
                {{ submitStatus.message }}
              </div>
            </form>
          </div>
        </div>
      </div>
    </section>

    <!-- Additional Info -->
    <section class="additional-info">
      <div class="container">
        <div class="info-grid">
          <div class="info-item">
            <div class="info-icon">🎯</div>
            <h3>What I'm Looking For</h3>
            <ul>
              <li>Internship opportunities in software development</li>
              <li>Collaborative projects with other developers</li>
              <li>
                Open source contribution opportunities (check my
                <a
                  href="https://github.com/eabhi-me"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="inline-link"
                  >GitHub</a
                >)
              </li>
              <li>Mentorship and learning opportunities</li>
            </ul>
          </div>

          <div class="info-item">
            <div class="info-icon">🚀</div>
            <h3>What I Can Offer</h3>
            <ul>
              <li>Fresh perspective on modern technologies</li>
              <li>Enthusiasm for learning and growth</li>
              <li>
                Strong foundation in web development (see my
                <a
                  href="https://brahamadevi.in"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="inline-link"
                  >projects</a
                >)
              </li>
              <li>Collaborative and team-oriented approach</li>
            </ul>
          </div>

          <div class="info-item">
            <div class="info-icon">⚡</div>
            <h3>Response Time</h3>
            <ul>
              <li>
                <a href="mailto:eabhi.me@gmail.com" class="inline-link">Email</a>: Within 24 hours
              </li>
              <li>
                <a
                  href="https://linkedin.com/in/eabhi-me/"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="inline-link"
                  >LinkedIn</a
                >: Within 48 hours
              </li>
              <li>Urgent matters: Please mention in subject</li>
              <li>Project discussions: Same day when possible</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQ Section -->
    <section class="faq-section">
      <div class="container">
        <h2 class="section-subtitle">Frequently Asked Questions</h2>

        <div class="faq-list">
          <div
            v-for="(faq, index) in faqs"
            :key="index"
            class="faq-item"
            :class="{ active: activeFaq === index }"
          >
            <button class="faq-question" @click="toggleFaq(index)">
              <span>{{ faq.question }}</span>
              <span class="faq-toggle">{{ activeFaq === index ? '−' : '+' }}</span>
            </button>
            <div class="faq-answer" v-show="activeFaq === index">
              <p>{{ faq.answer }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'ContactView',
  data() {
    return {
      form: {
        name: '',
        email: '',
        subject: '',
        message: '',
        newsletter: false,
      },
      isSubmitting: false,
      submitStatus: null,
      activeFaq: null,
      faqs: [
        {
          question: 'What type of projects are you interested in?',
          answer:
            "I'm particularly interested in web development projects, mobile applications, and anything involving modern JavaScript frameworks. I'm also excited about AI/ML projects and open-source contributions.",
        },
        {
          question: 'Are you available for full-time positions?',
          answer:
            "Currently, I'm focused on completing my engineering degree, so I'm primarily looking for internship opportunities, part-time positions, or project-based collaborations that can fit around my academic schedule.",
        },
        {
          question: "What's your preferred technology stack?",
          answer:
            "I'm most comfortable with JavaScript/TypeScript, Vue.js, React, Node.js, and modern web technologies. However, I'm always eager to learn new technologies and adapt to project requirements.",
        },
        {
          question: 'Do you work on freelance projects?',
          answer:
            "Yes! I'm open to freelance projects, especially those that allow me to learn new skills and work with interesting technologies. Feel free to reach out with your project details.",
        },
        {
          question: 'How do you handle project timelines?',
          answer:
            "I believe in clear communication and realistic timeline setting. I'll always be upfront about my availability and ensure that any commitments I make are ones I can definitely fulfill.",
        },
      ],
    }
  },
  methods: {
    async submitForm() {
      this.isSubmitting = true
      this.submitStatus = null

      try {
        // Simulate form submission (replace with actual API call)
        await new Promise((resolve) => setTimeout(resolve, 2000))

        this.submitStatus = {
          type: 'success',
          message: "Thank you! Your message has been sent successfully. I'll get back to you soon.",
        }

        // Reset form
        this.form = {
          name: '',
          email: '',
          subject: '',
          message: '',
          newsletter: false,
        }
      } catch (error) {
        this.submitStatus = {
          type: 'error',
          message:
            'Sorry, there was an error sending your message. Please try again or contact me directly.',
        }
      } finally {
        this.isSubmitting = false
      }
    },
    toggleFaq(index) {
      this.activeFaq = this.activeFaq === index ? null : index
    },
  },
}
</script>

<style scoped>
.contact {
  padding-top: 80px;
}

/* Hero Section */
.contact-hero {
  padding: 4rem 0;
  color: black;
  text-align: center;
}

.hero-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

.hero-subtitle {
  font-size: 1.2rem;
  font-weight: 300;
  opacity: 0.9;
  margin-top: 1rem;
}

.section-subtitle {
  font-size: 2rem;
  font-weight: 600;
  text-align: center;
  margin-bottom: 3rem;
  color: #2c3e50;
}

/* Contact Content */
.contact-content {
  padding: 5rem 0;
  background: white;
}

.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: start;
}

.contact-info h2 {
  font-size: 2rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 1.5rem;
}

.contact-description {
  font-size: 1.1rem;
  line-height: 1.8;
  color: #5a6c7d;
  margin-bottom: 2.5rem;
}

.contact-methods {
  margin-bottom: 3rem;
}

.contact-method {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1.5rem;
  margin-bottom: 1rem;
  background: #f8f9fa;
  border-radius: 15px;
  transition: transform 0.3s ease;
}

.contact-method:hover {
  transform: translateX(5px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.method-icon {
  font-size: 2rem;
  min-width: 60px;
  text-align: center;
}

.method-content h3 {
  font-size: 1.1rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 0.25rem;
}

.method-content p {
  color: #667eea;
  font-weight: 500;
  margin-bottom: 0.25rem;
}

.contact-link {
  color: #667eea;
  font-weight: 500;
  text-decoration: none;
  transition: all 0.3s ease;
  display: inline-block;
  margin-bottom: 0.25rem;
  padding: 0.25rem 0;
  border-bottom: 2px solid transparent;
}

.contact-link:hover {
  color: #5a67d8;
  border-bottom-color: #5a67d8;
  transform: translateX(3px);
}

.contact-link:focus {
  outline: 2px solid #667eea;
  outline-offset: 2px;
  border-radius: 4px;
}

.method-note {
  color: #7f8c8d;
  font-size: 0.9rem;
}

.availability {
  padding: 1.5rem;
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
  border-radius: 15px;
  border-left: 4px solid #28a745;
}

.availability h3 {
  font-size: 1.2rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 1rem;
}

.availability-status {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
}

.status-indicator {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: #28a745;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
  100% {
    opacity: 1;
  }
}

.availability-note {
  color: #5a6c7d;
  font-size: 0.95rem;
  line-height: 1.6;
}

/* Contact Form */
.contact-form-container {
  background: #f8f9fa;
  padding: 2.5rem;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.contact-form h2 {
  font-size: 1.8rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 2rem;
  text-align: center;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.form-input,
.form-select,
.form-textarea {
  width: 100%;
  padding: 1rem;
  border: 2px solid #e9ecef;
  border-radius: 10px;
  font-size: 1rem;
  transition:
    border-color 0.3s ease,
    box-shadow 0.3s ease;
  font-family: inherit;
}

.form-input:focus,
.form-select:focus,
.form-textarea:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.form-textarea {
  resize: vertical;
  min-height: 120px;
}

.checkbox-label {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  cursor: pointer;
  font-weight: normal;
}

.checkbox-input {
  display: none;
}

.checkbox-custom {
  width: 20px;
  height: 20px;
  border: 2px solid #e9ecef;
  border-radius: 4px;
  position: relative;
  transition: all 0.3s ease;
}

.checkbox-input:checked + .checkbox-custom {
  background: #667eea;
  border-color: #667eea;
}

.checkbox-input:checked + .checkbox-custom::after {
  content: '✓';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  font-size: 14px;
  font-weight: bold;
}

.submit-btn {
  width: 100%;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 1rem 2rem;
  border: none;
  border-radius: 10px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-bottom: 1rem;
}

.submit-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(102, 126, 234, 0.3);
}

.submit-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.submit-status {
  padding: 1rem;
  border-radius: 10px;
  font-weight: 500;
  text-align: center;
}

.submit-status.success {
  background: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
}

.submit-status.error {
  background: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}

/* Additional Info */
.additional-info {
  padding: 5rem 0;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

.info-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.info-item {
  background: white;
  padding: 2rem;
  border-radius: 15px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.info-item:hover {
  transform: translateY(-5px);
}

.info-icon {
  font-size: 3rem;
  text-align: center;
  margin-bottom: 1rem;
}

.info-item h3 {
  font-size: 1.3rem;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 1rem;
  text-align: center;
}

.info-item ul {
  list-style: none;
  padding: 0;
}

.info-item li {
  padding: 0.5rem 0;
  color: #5a6c7d;
  position: relative;
  padding-left: 1.5rem;
  line-height: 1.6;
}

.info-item li::before {
  content: '•';
  position: absolute;
  left: 0;
  color: #667eea;
  font-weight: bold;
}

.inline-link {
  color: #667eea;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s ease;
  border-bottom: 1px solid transparent;
}

.inline-link:hover {
  color: #5a67d8;
  border-bottom-color: #5a67d8;
}

.inline-link:focus {
  outline: 2px solid #667eea;
  outline-offset: 2px;
  border-radius: 2px;
}

/* FAQ Section */
.faq-section {
  padding: 5rem 0;
  background: white;
}

.faq-list {
  max-width: 1200px;
  margin: 0 auto;
}

.faq-item {
  margin-bottom: 1rem;
  border: 1px solid #e9ecef;
  border-radius: 10px;
  overflow: hidden;
  transition: all 0.3s ease;
}

.faq-item.active {
  border-color: #667eea;
  box-shadow: 0 5px 15px rgba(102, 126, 234, 0.1);
}

.faq-question {
  width: 100%;
  padding: 1.5rem;
  background: #f8f9fa;
  border: none;
  text-align: left;
  font-size: 1.1rem;
  font-weight: 600;
  color: #2c3e50;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: background-color 0.3s ease;
}

.faq-question:hover,
.faq-item.active .faq-question {
  background: #667eea;
  color: white;
}

.faq-toggle {
  font-size: 1.5rem;
  font-weight: bold;
  transition: transform 0.3s ease;
}

.faq-item.active .faq-toggle {
  transform: rotate(180deg);
}

.faq-answer {
  padding: 1.5rem;
  background: white;
  color: #5a6c7d;
  line-height: 1.7;
}

/* Responsive Design */
@media (max-width: 768px) {
  .contact-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }

  .contact-form-container {
    order: -1;
  }

  .info-grid {
    grid-template-columns: 1fr;
  }

  .contact-method {
    flex-direction: column;
    text-align: center;
  }
}

@media (max-width: 480px) {
  .contact {
    padding-top: 70px;
  }

  .contact-hero {
    padding: 2rem 0;
  }

  .contact-content,
  .additional-info,
  .faq-section {
    padding: 3rem 0;
  }

  .contact-form-container {
    padding: 1.5rem;
  }

  .faq-question {
    padding: 1rem;
    font-size: 1rem;
  }

  .faq-answer {
    padding: 1rem;
  }
}
</style>
