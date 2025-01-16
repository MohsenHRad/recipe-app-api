from datetime import date

from django.shortcuts import render

all_posts = [
    {
        'slug': 'learning-django',
        'title': 'django-course',
        'author': 'Mohsen.H.Rad',
        'image': 'django.png',
        'date': date(2023, 1, 20),
        'short_description': 'This is django course in Toplearn from zero to hero',
        'content': """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Autem deserunt dicta dignissimos dolores ducimus
            eum facilis harum iste nobis pariatur porro, quia, rem sapiente sed similique sit unde. Animi debitis, eos
            eum ipsum nesciunt odio officiis quam rerum sit vero?
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Autem deserunt dicta dignissimos dolores ducimus
            eum facilis harum iste nobis pariatur porro, quia, rem sapiente sed similique sit unde. Animi debitis, eos
            eum ipsum nesciunt odio officiis quam rerum sit vero?
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Autem deserunt dicta dignissimos dolores ducimus
            eum facilis harum iste nobis pariatur porro, quia, rem sapiente sed similique sit unde. Animi debitis, eos
            eum ipsum nesciunt odio officiis quam rerum sit vero?
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Autem deserunt dicta dignissimos dolores ducimus
        eum facilis harum iste nobis pariatur porro, quia, rem sapiente sed similique sit unde. Animi debitis, eos
        eum ipsum nesciunt odio officiis quam rerum sit vero?
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. Autem deserunt dicta dignissimos dolores ducimus
        eum facilis harum iste nobis pariatur porro, quia, rem sapiente sed similique sit unde. Animi debitis, eos
        eum ipsum nesciunt odio officiis quam rerum sit vero?
        """
    },
    {
        'slug': 'learning-machine-learning',
        'title': 'ml-course',
        'author': 'Mohsen.H.Rad',
        'image': 'ml.png',
        'date': date(2021, 11, 8),
        'short_description': 'This is machine-learning course in Toplearn from zero to hero',
        'content': """
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Autem deserunt dicta dignissimos dolores ducimus
        eum facilis harum iste nobis pariatur porro, quia, rem sapiente sed similique sit unde. Animi debitis, eos
        eum ipsum nesciunt odio officiis quam rerum sit vero?
    """
    }, {
        'slug': 'learning-python',
        'title': 'python-course',
        'author': 'Mohsen.H.Rad',
        'image': 'python.png',
        'date': date(2022, 10, 7),
        'short_description': 'This is python course in Toplearn from zero to hero',
        'content': """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Autem deserunt dicta dignissimos dolores ducimus
            eum facilis harum iste nobis pariatur porro, quia, rem sapiente sed similique sit unde. Animi debitis, eos
            eum ipsum nesciunt odio officiis quam rerum sit vero?
        """
    }

]


def get_date_of_post(post):
    return post['date']


# Create your views here.

def index(request):
    sorted_post = sorted(all_posts, key=get_date_of_post)
    latest_posts = sorted_post[-2:]
    return render(request, 'blog/index.html', {
        'latest_posts': latest_posts
    })


def posts(request):
    context = {
        'all_posts': all_posts
    }
    return render(request, 'blog/all-posts.html', context)


def single_post(request, slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {'post': post})
