# Blog Project

A blog system is composed of a series of posts that the user writes.

# Stack

- Python `>= 3.5`
- Django `>= 2.0`

# How to use this Repo

1. Fork this repo.
2. Add your files to the folder with your name in your own forked repo.
3. When you are done with the exercises, Send a pull request with this repository as the target.

# Project Sections

## Blog Index Page

This page will render a *paginated* list of all blog posts.

### Page specs:
    - Heading
    - Sub-heading
    - Post list
        - Title
        - Subtitle/Caption
        - Author
        - Date Created
        - Tags
        - Category
        - Link/Button to open the Post Details page

## Blog Post Page

This page will render all of a blog post's content.

### Page specs
    - Heading
    - Sub-heading
    - Banner photo
    - Author
    - Date Created
    - Date Modified
    - Tags (A post can have multiple tags)
    - Category (A post can have only 1 category)
    - Body (the main content)
    - Status (Published/Draft/Hidden)

# Optional Features

- Comment system on Blog Posts
    - Author (non-Django user. This can just be an email or any username)
    - Content
    - Date created

- Admin Panel for blog management (An admin panel created by the programmer, Django's Admin Panel excluded)
    - Create/Edit Blog Index content
    - Create/Edit Blog post content/details
