practical-neuroimaging.github.com
=================================

Web pages for Practical neuroimaging course.

The website is built using Sphinx.

The built web-pages go in the ``master`` branch of this repo.

The Sphinx source for the website goes in the ``source`` branch.

Working on the site goes like:

    git co source
    # Edit the files
    make html # Check what the pages look like
    make gh-pages # Push back to the master branch
    # Now on 'master' branch
    git commit
    git push # Push up web pages
    git co source # Back to editing if you want
