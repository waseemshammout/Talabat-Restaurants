-- Deleting duplicated url
while exists(select max(id) dID
             from talabat_restaurants_urls
             group by [url]
             having count(*) > 1)
    delete
    from [dbo].[talabat_restaurants_urls]
    where id in (select max(id) dID
                 from talabat_restaurants_urls
                 group by [url]
                 having count(*) > 1)