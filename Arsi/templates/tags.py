from django import template
from django.utils import timezone
from category.models import Category
from products.models import ProductStore, Color
from django.template.loader import render_to_string
from home.models import Social


register = template.Library()


@register.simple_tag
def assets():
    return 'assets-dark'
    if timezone.localtime().hour >= 18 or timezone.localtime().hour < 6:
        return 'assets-dark'
    else:
        return 'assets-light'


@register.simple_tag
def GlobalName(lang='fa'):
    if lang == 'fa':
        return 'ویرا'
    if lang == 'en':
        return 'Vira'


@register.simple_tag
def base_header(request):
    user =''
    if request.user.is_authenticated:
        user = request.user
    sub_categories = Category.objects.filter(parent_id=0)
    # main_catedories = Category.objects.filter(id=id,parent_id=sub_categories)
    carts = []
    count_cart = 0
    total_price = 0
    if 'cart' in request.session:
          for cart in request.session['cart']:
              count_cart +=1
              total_price +=int(cart['price'])
              product = ProductStore.objects.get(id=cart['product_store_id']).product
              product_store = ProductStore.objects.get(id=cart['product_store_id']).id
              color = None
              if cart['color_id'] is not 0:
                  color = Color.objects.get(id=cart['color_id'])
              item={'product':product,'color':color,'price':cart['price'],'product_store': product_store}
              carts.append(item)

    favorites = []
    count_favorite = 0
    if 'favorite' in request.session:
        for favorite in request.session['favorite']:
            count_favorite += 1
            product = ProductStore.objects.get(id=favorite['product_store_id']).product
            product_store = ProductStore.objects.get(id=favorite['product_store_id']).id
            item = {'product': product, 'product_store': product_store}
            favorites.append(item)

    compares = []
    count_compare = 0
    if 'compare' in request.session:
        for compare in request.session['compare']:
            count_compare += 1
            product = ProductStore.objects.get(id=compare['product_store_id']).product
            product_store = ProductStore.objects.get(id=compare['product_store_id']).id
            cate = product.main_category
            item = {'product': product, 'product_store': product_store, 'category': cate}
            compares.append(item)

    return render_to_string('sub/header.html', {'user':user,'sub_categories': sub_categories,'count_cart':count_cart,'carts':carts,'total_price':total_price,'favorites': favorites, 'count_favorite':count_favorite,'compares':compares,'count_compare':count_compare})

@register.simple_tag
def footer(request):
    categories = Category.objects.filter(parent_id=0)
    socials = Social.objects.all()
    return render_to_string('sub/footer.html',{'categories':categories,'socials':socials})

