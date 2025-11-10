---
hide:
  - footer
title: Fifth Printing
---

# Updates and Errata - Fifth printing

This page is broken into two parts, Updates and Errata. *Updates* address issues that affect whether your code will run or not. *Errata* refer to minor issues such as typos, and errors in grayed-out code that probably won’t affect the code you’re entering.

Code that produces warnings but still runs correctly is noted under Errata, as this is a fairly common occurrence and the code often still works for a long time while producing warnings.

If you find an error in the book that's not listed here, or can’t get something to work, please let me know. You can reach me through email at ehmatthes@gmail.com, or on Twitter at @ehmatthes.

- [Updates](#updates)
- [Errata](#errata)
    - [Chapter 16](#chapter-16)

---

Updates
---

There are no updates to note at this time.

---

Errata
---

### Chapter 16

On page 351, the line that starts the `for` loop over `all_eq_dicts` is missing. This line was shown in earlier listings, but was left out on this page.

The listing on page 351 should look like this:

```python
--snip--
mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)

title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
        --snip--
        projection='natural earth',
        hover_name=eq_titles,
    )
fig.show()
```
