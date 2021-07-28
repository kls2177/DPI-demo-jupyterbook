#!/usr/bin/env python
# coding: utf-8

# # Examples using `.ipynb` File:
# ## Markdown, Equations, Text Blocks and Code:
# 
# *There are several examples below that demonstrate different features of* `jupyterbook`.
# 
# ----------------------------------------------
# ## Markdown
# ### Example 1: Introduction to Programming in Python
# 
# <font color=red>**When you want to just have text, insert a Markdown cell. see the text below for different font examples.**</font>
# 
# In Part I, we will cover the fundamentals of python. Note that this is workshop is not exhaustive, but it will provide you with a useful introduction. There aren many, **many**, python tutorials, courses, etc. online, so if you are interested in learning more, a quick google search is all you need do.
# 
# Most of the output on this webpage is *hidden* in order to give you the opportunity to think the code through before you click to reveal the output. And remember, <font color=green>***press Shift-Enter to run the code***</font>.
# 
# Follow along in your own blank jupyter notebook or click on the "Live Code/Launch Thebe" button in the upper right corner. **It takes a few minutes for the "Live Code" session to launch**.
# 
# Let's start with a simple hello world program (just as we did in the video). 
# 
# Note that `#` followed by text is a **comment**. The `#` sympbol tells python not to interpret this line as code.

# ----------------------------------------------
# ## Equations and Text Blocks
# ### Example 2: The Central Limit Theorem
# 
# <font color=red>**To insert equations, you can use the `mathmode` by starting and ending your equation with `$$` and using LaTeX syntax to write your equation:**</font>

# Recall that the $z$-statistic is defined as,
# 
# $$
# z = \frac{x - \mu}{\sigma}
# $$
# 
# where $\mu$ is the population mean and $\sigma$ is the population standard deviation and $x$ is normally distributed.
# 
# As we noted above, we are usually not interested in a specific value, $x$, but rather a sample mean, $\overline{x}$. So, can we substitute $x$ for $\overline{x}$ and use the $z$-table to test our null hypothesis? Almost...There are a few things we need to address first:
# - How do we know if $\overline{x}$ is normally distributed?
# - Does the underlying population of $\overline{x}$ have the same mean and standard deviation as $x$?

# <font color=red>**If you want to insert a specialized text block use the `admonition` feature:**</font>

# Fortunately, we have a theorem for this: **The Central Limit Theorem**
# 
# ```{admonition} The Central Limit Theorem
# :class: note
# Given a sample of size $N$ drawn from a distribution with known population mean $\mu$ and known population standard deviation, $\sigma$, if the size ($N$) of the sample is sufficiently large, then the distribution of the sample means will approximate a normal distribution regardless of the underlying distribution of the population. The mean of the sample means will equal the population mean, $\mu$, and the standard deviation of the distribution of the sample means will equal the standard error, $\sigma/\sqrt{N}$.
# ```
# 
# In other words, the Central Limit Theorem (CLT) says that if you have a sample that is large enough, you can use the normally distributed $z$-statistic to estimate probabilities of getting that sample mean - no matter the distribution of the underlying data.

# ----------------------------------------------
# ## Code and Hidden Input/Output
# ### Example 3: Introduction to Programming in Python (cont'd)

# <font color=red>**When you want to embed code, just insert a code cell.**</font>

# In[1]:


# this is a comment
print("Hello World!")


# <font color=red>**You can use tags to hide the input, output or both.**</font>

# In[2]:


# this is a comment
print("Hello World!")


# <font color=red>**Use standard python syntax to load packages. Be sure that the packages you want to load are included in the `requirements.txt` file.**</font>

# In[3]:


# Load packages
import numpy as np
from matplotlib import pyplot as plt


# <font color=red>**Finally, here is an example of generating a plot.**</font>

# We are going to draw samples of data from three different distributions, a normal distribution, a uniform distribution and a lognormal distribution. Each sample is of size $N_0$.

# In[4]:


N0 = 10000000
xinc = np.arange(-10,10,.01) # bin size

# We are drawing large samples from a normal, a uniform and a log-normal distribution.

xn = np.random.normal(0,1,size = (N0,))
xu = np.random.uniform(-5.,5.,size=(N0,))
xl = np.random.lognormal(0.,2.,size=(N0,))


# Let's compute the histograms and plot the PDFs of each of these data sets to see what they look like.

# In[5]:


# Calculate histograms

hn = np.histogram(xn,xinc)
hu = np.histogram(xu,xinc)
hl = np.histogram(xl,xinc)


# In[6]:


# Plot the PDFs (in terms of frequency)

plt.figure(figsize=(10,6))
plt.ylabel('Frequency')
plt.xlim(-8,8)

# Plot normal distribution
plt.plot(hn[1][:-1],hn[0]/N0,'-',color='black', label = 'normal')

# Plot uniform distribution
plt.plot(hu[1][:-1],hu[0]/N0,'-',color='blue',label = 'uniform')

# Plot log-normal distribution
plt.plot(hl[1][:-1],hl[0]/N0,'-',color='orange', label='lognormal')

# Add a legened
plt.legend(fontsize = 15)
plt.tight_layout()


# In[ ]:




