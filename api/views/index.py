from django.shortcuts import render

from api.list_urls import list_urls, urlconf


def sitemap_view(request):
    request_filter = request.GET.get("filter", None)

    raw_urls = list(list_urls(urlconf.urlpatterns))
    urls = []
    for uri in raw_urls:
        joined_url = "".join(uri)

        # Exclude admin routes
        if joined_url.startswith("admin/") and joined_url != "admin/":
            continue

        # Exclude swagger routing
        elif joined_url.startswith("^"):
            continue

        # Apply filters
        if request_filter and not joined_url.startswith(request_filter):
            continue

        # joined_url = joined_url.replace("<slug:slug>", "slug_here")
        # joined_url = joined_url.replace("<str:username>", "username_here")

        urls.append(joined_url)

    urls = sorted(urls)

    return render(request, "api/sitemap.html", context={"all_urls": urls})
