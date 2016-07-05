<h3>Floyd's Dreams of Dylan</h3>
<h1>{{ album.get('name') }}</h1>
<img src="{{ album.get('bibframe:CoverArt').get('url') }}" style="float:right">
<h2>Tracks</h2>
<ol>
% for track in album.get('track', []):
 <li><a href="{{ track.get('url') }}">{{ track.get('name') }}</a> {{ track.get('duration') }}</li>
% end
</ol>
[<a href="/">Home</a>|<a href="/dylans-head">Inside Dylan's Head</a>|<a href="/title-island">Title Island</a>|<a href="/lucid-dreamer">Floyd's Lucid Dream</a>]
<p><strong>&copy; 2012, 2013- Jeremy Nelson, Floyd Shiery</strong></p>
%rebase layout title="{{ album.get('name') }}"
