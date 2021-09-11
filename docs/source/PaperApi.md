# s2cholar.PaperApi

All URIs are relative to *https://localhost/graph/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_graph_get_paper**](PaperApi.md#get_graph_get_paper) | **GET** /paper/{paper_id} | Details about a paper
[**get_graph_get_paper_authors**](PaperApi.md#get_graph_get_paper_authors) | **GET** /paper/{paper_id}/authors | Details about a paper&#39;s authors
[**get_graph_get_paper_citations**](PaperApi.md#get_graph_get_paper_citations) | **GET** /paper/{paper_id}/citations | Details about a paper&#39;s citations
[**get_graph_get_paper_references**](PaperApi.md#get_graph_get_paper_references) | **GET** /paper/{paper_id}/references | Details about a paper&#39;s references
[**get_graph_get_paper_search**](PaperApi.md#get_graph_get_paper_search) | **GET** /paper/search | Search for papers by keyword


# **get_graph_get_paper**
> FullPaper get_graph_get_paper(paper_id, fields=fields)

Details about a paper

### Example
```python
from __future__ import print_function
import time
import s2cholar
from s2cholar.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = s2cholar.PaperApi()
paper_id = 'paper_id_example' # str | The following types of IDs are supported: <ul>     <li><code>&lt;sha&gt;</code> - a Semantic Scholar ID, e.g. <code>649def34f8be52c8b66281af98ae884c09aef38b</code></li>     <li><code>CorpusId:&lt;id&gt;</code> - Semantic Scholar numerical ID, e.g. <code>215416146</code></li>     <li><code>DOI:&lt;doi&gt;</code> - a <a href=\"http://doi.org\">Digital Object Identifier</a>,         e.g. <code>DOI:10.18653/v1/N18-3011</code></li>     <li><code>ARXIV:&lt;id&gt;</code> - <a href=\"https://arxiv.org/\">arXiv.rg</a>, e.g. <code>ARXIV:2106.15928</code></li>     <li><code>MAG:&lt;id&gt;</code> - Microsoft Academic Graph, e.g. <code>MAG:112218234</code></li>     <li><code>ACL:&lt;id&gt;</code> - Association for Computational Linguistics, e.g. <code>ACL:W12-3903</code></li>     <li><code>PMID:&lt;id&gt;</code> - PubMed/Medline, e.g. <code>PMID:19872477</code></li>     <li><code>PMCID:&lt;id&gt;</code> - PubMed Central, e.g. <code>PMCID:2323736</code></li>     <li><code>URL:&lt;url&gt;</code> - URL from one of the sites listed below, e.g. <code>URL:https://arxiv.org/abs/2106.15928v1</code></li> </ul>  URLs are recognized from the following sites: <ul>     <li><a href=\"https://www.semanticscholar.org/\">semanticscholar.org</a></li>     <li><a href=\"https://arxiv.org/\">arxiv.org</a></li>     <li><a href=\"https://www.aclweb.org\">aclweb.org</a></li>     <li><a href=\"https://www.acm.org/\">acm.org</a></li>     <li><a href=\"https://www.biorxiv.org/\">biorxiv.org</a></li> </ul>
fields = 'fields_example' # str | A comma-separated list of the fields to be returned.<br><br>  The following case-sensitive paper fields are recognized: <ul>     <li><code>paperId</code> - Always included</li>     <li><code>externalIds</code></li>     <li><code>url</code></li>     <li><code>title</code> - Included if no fields are specified</li>     <li><code>abstract</code></li>     <li><code>venue</code></li>     <li><code>year</code></li>     <li><code>referenceCount</code></li>     <li><code>citationCount</code></li>     <li><code>influentialCitationCount</code></li>     <li><code>isOpenAccess</code></li>     <li><code>fieldsOfStudy</code></li>     <li><code>authors</code> - Up to 500 will be returned</li>         <ul>             <li><code>authorId</code> - Always included</li>             <li><code>externalIds</code></li>             <li><code>url</code></li>             <li><code>name</code> - Included if no fields are specified</li>             <li><code>aliases</code></li>             <li><code>affiliations</code></li>             <li><code>homepage</code></li>             <li>To get more detailed information about a paper's authors, use the <code>/paper/{paper_id}/authors</code> endpoint</li>         </ul>     <li><code>citations</code> - Up to 1000 will be returned</li>         <ul>             <li><code>paperId</code> - Always included</li>             <li><code>url</code></li>             <li><code>title</code> - Included if no fields are specified</li>             <li><code>venue</code></li>             <li><code>year</code></li>             <li><code>authors</code> - Will include: <code>authorId</code> & <code>name</code></li>             <li>To get more detailed information about a paper's citations, use the <code>/paper/{paper_id}/citations</code> endpoint</li>         </ul>     <li><code>references</code> - Up to 1000 will be returned</li>         <ul>             <li><code>paperId</code> - Always included</li>             <li><code>url</code></li>             <li><code>title</code> - Included if no fields are specified</li>             <li><code>venue</code></li>             <li><code>year</code></li>             <li><code>authors</code> - Will include: <code>authorId</code> & <code>name</code></li>             <li>To get more detailed information about a paper's references, use the <code>/paper/{paper_id}/references</code> endpoint</li>         </ul>     <li><code>embedding</code></li> </ul> <br><br> Examples: <ul>     <li><code>https://api.semanticscholar.org/graph/v1/paper/649def34f8be52c8b66281af98ae884c09aef38b</code></li>     <ul>         <li>Returns the paper's always included field of paperId plus its title.  </li>     </ul>     <li><code>https://api.semanticscholar.org/graph/v1/paper/649def34f8be52c8b66281af98ae884c09aef38b?fields=url,year,authors</code></li>     <ul>         <li>Returns the paper's paperId, url, year, and list of authors.  </li>         <li>Each author has authorId and name.</li>     </ul>     <li><code>https://api.semanticscholar.org/graph/v1/paper/649def34f8be52c8b66281af98ae884c09aef38b?fields=citations.authors</code></li>     <ul>         <li>Returns the paper's paperId and list of citations.  </li>         <li>Each citation has its paperId plus its list of authors.</li>         <li>Each author has their 2 always included fields of authorId and name.</li>     </ul> </ul> (optional)

try:
    # Details about a paper
    api_response = api_instance.get_graph_get_paper(paper_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaperApi->get_graph_get_paper: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paper_id** | **str**| The following types of IDs are supported: &lt;ul&gt;     &lt;li&gt;&lt;code&gt;&amp;lt;sha&amp;gt;&lt;/code&gt; - a Semantic Scholar ID, e.g. &lt;code&gt;649def34f8be52c8b66281af98ae884c09aef38b&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;CorpusId:&amp;lt;id&amp;gt;&lt;/code&gt; - Semantic Scholar numerical ID, e.g. &lt;code&gt;215416146&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;DOI:&amp;lt;doi&amp;gt;&lt;/code&gt; - a &lt;a href&#x3D;\&quot;http://doi.org\&quot;&gt;Digital Object Identifier&lt;/a&gt;,         e.g. &lt;code&gt;DOI:10.18653/v1/N18-3011&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;ARXIV:&amp;lt;id&amp;gt;&lt;/code&gt; - &lt;a href&#x3D;\&quot;https://arxiv.org/\&quot;&gt;arXiv.rg&lt;/a&gt;, e.g. &lt;code&gt;ARXIV:2106.15928&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;MAG:&amp;lt;id&amp;gt;&lt;/code&gt; - Microsoft Academic Graph, e.g. &lt;code&gt;MAG:112218234&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;ACL:&amp;lt;id&amp;gt;&lt;/code&gt; - Association for Computational Linguistics, e.g. &lt;code&gt;ACL:W12-3903&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;PMID:&amp;lt;id&amp;gt;&lt;/code&gt; - PubMed/Medline, e.g. &lt;code&gt;PMID:19872477&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;PMCID:&amp;lt;id&amp;gt;&lt;/code&gt; - PubMed Central, e.g. &lt;code&gt;PMCID:2323736&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;URL:&amp;lt;url&amp;gt;&lt;/code&gt; - URL from one of the sites listed below, e.g. &lt;code&gt;URL:https://arxiv.org/abs/2106.15928v1&lt;/code&gt;&lt;/li&gt; &lt;/ul&gt;  URLs are recognized from the following sites: &lt;ul&gt;     &lt;li&gt;&lt;a href&#x3D;\&quot;https://www.semanticscholar.org/\&quot;&gt;semanticscholar.org&lt;/a&gt;&lt;/li&gt;     &lt;li&gt;&lt;a href&#x3D;\&quot;https://arxiv.org/\&quot;&gt;arxiv.org&lt;/a&gt;&lt;/li&gt;     &lt;li&gt;&lt;a href&#x3D;\&quot;https://www.aclweb.org\&quot;&gt;aclweb.org&lt;/a&gt;&lt;/li&gt;     &lt;li&gt;&lt;a href&#x3D;\&quot;https://www.acm.org/\&quot;&gt;acm.org&lt;/a&gt;&lt;/li&gt;     &lt;li&gt;&lt;a href&#x3D;\&quot;https://www.biorxiv.org/\&quot;&gt;biorxiv.org&lt;/a&gt;&lt;/li&gt; &lt;/ul&gt; |
 **fields** | **str**| A comma-separated list of the fields to be returned.&lt;br&gt;&lt;br&gt;  The following case-sensitive paper fields are recognized: &lt;ul&gt;     &lt;li&gt;&lt;code&gt;paperId&lt;/code&gt; - Always included&lt;/li&gt;     &lt;li&gt;&lt;code&gt;externalIds&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;url&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;title&lt;/code&gt; - Included if no fields are specified&lt;/li&gt;     &lt;li&gt;&lt;code&gt;abstract&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;venue&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;year&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;referenceCount&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;citationCount&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;influentialCitationCount&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;isOpenAccess&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;fieldsOfStudy&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;authors&lt;/code&gt; - Up to 500 will be returned&lt;/li&gt;         &lt;ul&gt;             &lt;li&gt;&lt;code&gt;authorId&lt;/code&gt; - Always included&lt;/li&gt;             &lt;li&gt;&lt;code&gt;externalIds&lt;/code&gt;&lt;/li&gt;             &lt;li&gt;&lt;code&gt;url&lt;/code&gt;&lt;/li&gt;             &lt;li&gt;&lt;code&gt;name&lt;/code&gt; - Included if no fields are specified&lt;/li&gt;             &lt;li&gt;&lt;code&gt;aliases&lt;/code&gt;&lt;/li&gt;             &lt;li&gt;&lt;code&gt;affiliations&lt;/code&gt;&lt;/li&gt;             &lt;li&gt;&lt;code&gt;homepage&lt;/code&gt;&lt;/li&gt;             &lt;li&gt;To get more detailed information about a paper&#39;s authors, use the &lt;code&gt;/paper/{paper_id}/authors&lt;/code&gt; endpoint&lt;/li&gt;         &lt;/ul&gt;     &lt;li&gt;&lt;code&gt;citations&lt;/code&gt; - Up to 1000 will be returned&lt;/li&gt;         &lt;ul&gt;             &lt;li&gt;&lt;code&gt;paperId&lt;/code&gt; - Always included&lt;/li&gt;             &lt;li&gt;&lt;code&gt;url&lt;/code&gt;&lt;/li&gt;             &lt;li&gt;&lt;code&gt;title&lt;/code&gt; - Included if no fields are specified&lt;/li&gt;             &lt;li&gt;&lt;code&gt;venue&lt;/code&gt;&lt;/li&gt;             &lt;li&gt;&lt;code&gt;year&lt;/code&gt;&lt;/li&gt;             &lt;li&gt;&lt;code&gt;authors&lt;/code&gt; - Will include: &lt;code&gt;authorId&lt;/code&gt; &amp; &lt;code&gt;name&lt;/code&gt;&lt;/li&gt;             &lt;li&gt;To get more detailed information about a paper&#39;s citations, use the &lt;code&gt;/paper/{paper_id}/citations&lt;/code&gt; endpoint&lt;/li&gt;         &lt;/ul&gt;     &lt;li&gt;&lt;code&gt;references&lt;/code&gt; - Up to 1000 will be returned&lt;/li&gt;         &lt;ul&gt;             &lt;li&gt;&lt;code&gt;paperId&lt;/code&gt; - Always included&lt;/li&gt;             &lt;li&gt;&lt;code&gt;url&lt;/code&gt;&lt;/li&gt;             &lt;li&gt;&lt;code&gt;title&lt;/code&gt; - Included if no fields are specified&lt;/li&gt;             &lt;li&gt;&lt;code&gt;venue&lt;/code&gt;&lt;/li&gt;             &lt;li&gt;&lt;code&gt;year&lt;/code&gt;&lt;/li&gt;             &lt;li&gt;&lt;code&gt;authors&lt;/code&gt; - Will include: &lt;code&gt;authorId&lt;/code&gt; &amp; &lt;code&gt;name&lt;/code&gt;&lt;/li&gt;             &lt;li&gt;To get more detailed information about a paper&#39;s references, use the &lt;code&gt;/paper/{paper_id}/references&lt;/code&gt; endpoint&lt;/li&gt;         &lt;/ul&gt;     &lt;li&gt;&lt;code&gt;embedding&lt;/code&gt;&lt;/li&gt; &lt;/ul&gt; &lt;br&gt;&lt;br&gt; Examples: &lt;ul&gt;     &lt;li&gt;&lt;code&gt;https://api.semanticscholar.org/graph/v1/paper/649def34f8be52c8b66281af98ae884c09aef38b&lt;/code&gt;&lt;/li&gt;     &lt;ul&gt;         &lt;li&gt;Returns the paper&#39;s always included field of paperId plus its title.  &lt;/li&gt;     &lt;/ul&gt;     &lt;li&gt;&lt;code&gt;https://api.semanticscholar.org/graph/v1/paper/649def34f8be52c8b66281af98ae884c09aef38b?fields&#x3D;url,year,authors&lt;/code&gt;&lt;/li&gt;     &lt;ul&gt;         &lt;li&gt;Returns the paper&#39;s paperId, url, year, and list of authors.  &lt;/li&gt;         &lt;li&gt;Each author has authorId and name.&lt;/li&gt;     &lt;/ul&gt;     &lt;li&gt;&lt;code&gt;https://api.semanticscholar.org/graph/v1/paper/649def34f8be52c8b66281af98ae884c09aef38b?fields&#x3D;citations.authors&lt;/code&gt;&lt;/li&gt;     &lt;ul&gt;         &lt;li&gt;Returns the paper&#39;s paperId and list of citations.  &lt;/li&gt;         &lt;li&gt;Each citation has its paperId plus its list of authors.&lt;/li&gt;         &lt;li&gt;Each author has their 2 always included fields of authorId and name.&lt;/li&gt;     &lt;/ul&gt; &lt;/ul&gt; | [optional]

### Return type

[**FullPaper**](FullPaper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)

# **get_graph_get_paper_authors**
> AuthorBatch get_graph_get_paper_authors(paper_id, offset=offset, limit=limit, fields=fields)

Details about a paper's authors

### Example
```python
from __future__ import print_function
import time
import s2cholar
from s2cholar.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = s2cholar.PaperApi()
paper_id = 'paper_id_example' # str | The following types of IDs are supported: <ul>     <li><code>&lt;sha&gt;</code> - a Semantic Scholar ID, e.g. <code>649def34f8be52c8b66281af98ae884c09aef38b</code></li>     <li><code>CorpusId:&lt;id&gt;</code> - Semantic Scholar numerical ID, e.g. <code>215416146</code></li>     <li><code>DOI:&lt;doi&gt;</code> - a <a href=\"http://doi.org\">Digital Object Identifier</a>,         e.g. <code>DOI:10.18653/v1/N18-3011</code></li>     <li><code>ARXIV:&lt;id&gt;</code> - <a href=\"https://arxiv.org/\">arXiv.rg</a>, e.g. <code>ARXIV:2106.15928</code></li>     <li><code>MAG:&lt;id&gt;</code> - Microsoft Academic Graph, e.g. <code>MAG:112218234</code></li>     <li><code>ACL:&lt;id&gt;</code> - Association for Computational Linguistics, e.g. <code>ACL:W12-3903</code></li>     <li><code>PMID:&lt;id&gt;</code> - PubMed/Medline, e.g. <code>PMID:19872477</code></li>     <li><code>PMCID:&lt;id&gt;</code> - PubMed Central, e.g. <code>PMCID:2323736</code></li>     <li><code>URL:&lt;url&gt;</code> - URL from one of the sites listed below, e.g. <code>URL:https://arxiv.org/abs/2106.15928v1</code></li> </ul>  URLs are recognized from the following sites: <ul>     <li><a href=\"https://www.semanticscholar.org/\">semanticscholar.org</a></li>     <li><a href=\"https://arxiv.org/\">arxiv.org</a></li>     <li><a href=\"https://www.aclweb.org\">aclweb.org</a></li>     <li><a href=\"https://www.acm.org/\">acm.org</a></li>     <li><a href=\"https://www.biorxiv.org/\">biorxiv.org</a></li> </ul>
offset = 0 # int | When returning a list of results, start with the element at this position in the list. (optional) (default to 0)
limit = 100 # int | The maximum number of results to return. (optional) (default to 100)
fields = 'fields_example' # str | A comma-separated list of the fields to be returned.<br><br> The following case-sensitive author fields are recognized: <ul>     <li><code>authorId</code> - Always included</li>     <li><code>externalIds</code></li>     <li><code>url</code></li>     <li><code>name</code> - Included if no fields are specified</li>     <li><code>aliases</code></li>     <li><code>affiliations</code></li>     <li><code>homepage</code></li>     <li><code>papers</code></li>     <ul>         <li><code>paperId</code> - Always included</li>         <li><code>externalIds</code></li>         <li><code>url</code></li>         <li><code>title</code> - Included if no fields are specified</li>         <li><code>abstract</code></li>         <li><code>venue</code></li>         <li><code>year</code></li>         <li><code>referenceCount</code></li>         <li><code>citationCount</code></li>         <li><code>influentialCitationCount</code></li>         <li><code>isOpenAccess</code></li>         <li><code>fieldsOfStudy</code></li>         <li><code>authors</code> - Will include: <code>authorId</code> & <code>name</code></li>     </ul> </ul> <br><br> Examples: <ul>     <li><code>https://api.semanticscholar.org/graph/v1/paper/649def34f8be52c8b66281af98ae884c09aef38b/authors</code></li>     <ul>         <li>Returns with offset=0, and data is a list of all 3 authors.</li>         <li>Each author has their authorId and name</li>     </ul>     <li><code>https://api.semanticscholar.org/graph/v1/paper/649def34f8be52c8b66281af98ae884c09aef38b/authors?fields=affiliations,papers&limit=2</code></li>     <ul>         <li>Returns with offset=0, next=2, and data is a list of 2 authors.</li>         <li>Each author has their authorId, affiliations, and list of papers.</li>         <li>Each paper has its paperId and title.</li>     </ul>     <li><code>https://api.semanticscholar.org/graph/v1/paper/649def34f8be52c8b66281af98ae884c09aef38b/authors?fields=url,papers.year,papers.authors&offset=2</code></li>     <ul>         <li>Returns with offset=2, and data is a list containing the last author.</li>         <li>This author has their authorId, url, and list of papers.</li>         <li>Each paper has its paperId, year, and list of authors.</li>         <li>In that list of authors, each author has their authorId and name.</li>     </ul> </ul> (optional)

try:
    # Details about a paper's authors
    api_response = api_instance.get_graph_get_paper_authors(paper_id, offset=offset, limit=limit, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaperApi->get_graph_get_paper_authors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paper_id** | **str**| The following types of IDs are supported: &lt;ul&gt;     &lt;li&gt;&lt;code&gt;&amp;lt;sha&amp;gt;&lt;/code&gt; - a Semantic Scholar ID, e.g. &lt;code&gt;649def34f8be52c8b66281af98ae884c09aef38b&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;CorpusId:&amp;lt;id&amp;gt;&lt;/code&gt; - Semantic Scholar numerical ID, e.g. &lt;code&gt;215416146&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;DOI:&amp;lt;doi&amp;gt;&lt;/code&gt; - a &lt;a href&#x3D;\&quot;http://doi.org\&quot;&gt;Digital Object Identifier&lt;/a&gt;,         e.g. &lt;code&gt;DOI:10.18653/v1/N18-3011&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;ARXIV:&amp;lt;id&amp;gt;&lt;/code&gt; - &lt;a href&#x3D;\&quot;https://arxiv.org/\&quot;&gt;arXiv.rg&lt;/a&gt;, e.g. &lt;code&gt;ARXIV:2106.15928&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;MAG:&amp;lt;id&amp;gt;&lt;/code&gt; - Microsoft Academic Graph, e.g. &lt;code&gt;MAG:112218234&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;ACL:&amp;lt;id&amp;gt;&lt;/code&gt; - Association for Computational Linguistics, e.g. &lt;code&gt;ACL:W12-3903&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;PMID:&amp;lt;id&amp;gt;&lt;/code&gt; - PubMed/Medline, e.g. &lt;code&gt;PMID:19872477&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;PMCID:&amp;lt;id&amp;gt;&lt;/code&gt; - PubMed Central, e.g. &lt;code&gt;PMCID:2323736&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;URL:&amp;lt;url&amp;gt;&lt;/code&gt; - URL from one of the sites listed below, e.g. &lt;code&gt;URL:https://arxiv.org/abs/2106.15928v1&lt;/code&gt;&lt;/li&gt; &lt;/ul&gt;  URLs are recognized from the following sites: &lt;ul&gt;     &lt;li&gt;&lt;a href&#x3D;\&quot;https://www.semanticscholar.org/\&quot;&gt;semanticscholar.org&lt;/a&gt;&lt;/li&gt;     &lt;li&gt;&lt;a href&#x3D;\&quot;https://arxiv.org/\&quot;&gt;arxiv.org&lt;/a&gt;&lt;/li&gt;     &lt;li&gt;&lt;a href&#x3D;\&quot;https://www.aclweb.org\&quot;&gt;aclweb.org&lt;/a&gt;&lt;/li&gt;     &lt;li&gt;&lt;a href&#x3D;\&quot;https://www.acm.org/\&quot;&gt;acm.org&lt;/a&gt;&lt;/li&gt;     &lt;li&gt;&lt;a href&#x3D;\&quot;https://www.biorxiv.org/\&quot;&gt;biorxiv.org&lt;/a&gt;&lt;/li&gt; &lt;/ul&gt; |
 **offset** | **int**| When returning a list of results, start with the element at this position in the list. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to return. | [optional] [default to 100]
 **fields** | **str**| A comma-separated list of the fields to be returned.&lt;br&gt;&lt;br&gt; The following case-sensitive author fields are recognized: &lt;ul&gt;     &lt;li&gt;&lt;code&gt;authorId&lt;/code&gt; - Always included&lt;/li&gt;     &lt;li&gt;&lt;code&gt;externalIds&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;url&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;name&lt;/code&gt; - Included if no fields are specified&lt;/li&gt;     &lt;li&gt;&lt;code&gt;aliases&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;affiliations&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;homepage&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;papers&lt;/code&gt;&lt;/li&gt;     &lt;ul&gt;         &lt;li&gt;&lt;code&gt;paperId&lt;/code&gt; - Always included&lt;/li&gt;         &lt;li&gt;&lt;code&gt;externalIds&lt;/code&gt;&lt;/li&gt;         &lt;li&gt;&lt;code&gt;url&lt;/code&gt;&lt;/li&gt;         &lt;li&gt;&lt;code&gt;title&lt;/code&gt; - Included if no fields are specified&lt;/li&gt;         &lt;li&gt;&lt;code&gt;abstract&lt;/code&gt;&lt;/li&gt;         &lt;li&gt;&lt;code&gt;venue&lt;/code&gt;&lt;/li&gt;         &lt;li&gt;&lt;code&gt;year&lt;/code&gt;&lt;/li&gt;         &lt;li&gt;&lt;code&gt;referenceCount&lt;/code&gt;&lt;/li&gt;         &lt;li&gt;&lt;code&gt;citationCount&lt;/code&gt;&lt;/li&gt;         &lt;li&gt;&lt;code&gt;influentialCitationCount&lt;/code&gt;&lt;/li&gt;         &lt;li&gt;&lt;code&gt;isOpenAccess&lt;/code&gt;&lt;/li&gt;         &lt;li&gt;&lt;code&gt;fieldsOfStudy&lt;/code&gt;&lt;/li&gt;         &lt;li&gt;&lt;code&gt;authors&lt;/code&gt; - Will include: &lt;code&gt;authorId&lt;/code&gt; &amp; &lt;code&gt;name&lt;/code&gt;&lt;/li&gt;     &lt;/ul&gt; &lt;/ul&gt; &lt;br&gt;&lt;br&gt; Examples: &lt;ul&gt;     &lt;li&gt;&lt;code&gt;https://api.semanticscholar.org/graph/v1/paper/649def34f8be52c8b66281af98ae884c09aef38b/authors&lt;/code&gt;&lt;/li&gt;     &lt;ul&gt;         &lt;li&gt;Returns with offset&#x3D;0, and data is a list of all 3 authors.&lt;/li&gt;         &lt;li&gt;Each author has their authorId and name&lt;/li&gt;     &lt;/ul&gt;     &lt;li&gt;&lt;code&gt;https://api.semanticscholar.org/graph/v1/paper/649def34f8be52c8b66281af98ae884c09aef38b/authors?fields&#x3D;affiliations,papers&amp;limit&#x3D;2&lt;/code&gt;&lt;/li&gt;     &lt;ul&gt;         &lt;li&gt;Returns with offset&#x3D;0, next&#x3D;2, and data is a list of 2 authors.&lt;/li&gt;         &lt;li&gt;Each author has their authorId, affiliations, and list of papers.&lt;/li&gt;         &lt;li&gt;Each paper has its paperId and title.&lt;/li&gt;     &lt;/ul&gt;     &lt;li&gt;&lt;code&gt;https://api.semanticscholar.org/graph/v1/paper/649def34f8be52c8b66281af98ae884c09aef38b/authors?fields&#x3D;url,papers.year,papers.authors&amp;offset&#x3D;2&lt;/code&gt;&lt;/li&gt;     &lt;ul&gt;         &lt;li&gt;Returns with offset&#x3D;2, and data is a list containing the last author.&lt;/li&gt;         &lt;li&gt;This author has their authorId, url, and list of papers.&lt;/li&gt;         &lt;li&gt;Each paper has its paperId, year, and list of authors.&lt;/li&gt;         &lt;li&gt;In that list of authors, each author has their authorId and name.&lt;/li&gt;     &lt;/ul&gt; &lt;/ul&gt; | [optional]

### Return type

[**AuthorBatch**](AuthorBatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)

# **get_graph_get_paper_citations**
> CitationBatch get_graph_get_paper_citations(paper_id, offset=offset, limit=limit, fields=fields)

Details about a paper's citations

Fetch details about the papers the cite this paper (i.e. papers in whose bibliography this paper appears)

### Example
```python
from __future__ import print_function
import time
import s2cholar
from s2cholar.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = s2cholar.PaperApi()
paper_id = 'paper_id_example' # str | The following types of IDs are supported: <ul>     <li><code>&lt;sha&gt;</code> - a Semantic Scholar ID, e.g. <code>649def34f8be52c8b66281af98ae884c09aef38b</code></li>     <li><code>CorpusId:&lt;id&gt;</code> - Semantic Scholar numerical ID, e.g. <code>215416146</code></li>     <li><code>DOI:&lt;doi&gt;</code> - a <a href=\"http://doi.org\">Digital Object Identifier</a>,         e.g. <code>DOI:10.18653/v1/N18-3011</code></li>     <li><code>ARXIV:&lt;id&gt;</code> - <a href=\"https://arxiv.org/\">arXiv.rg</a>, e.g. <code>ARXIV:2106.15928</code></li>     <li><code>MAG:&lt;id&gt;</code> - Microsoft Academic Graph, e.g. <code>MAG:112218234</code></li>     <li><code>ACL:&lt;id&gt;</code> - Association for Computational Linguistics, e.g. <code>ACL:W12-3903</code></li>     <li><code>PMID:&lt;id&gt;</code> - PubMed/Medline, e.g. <code>PMID:19872477</code></li>     <li><code>PMCID:&lt;id&gt;</code> - PubMed Central, e.g. <code>PMCID:2323736</code></li>     <li><code>URL:&lt;url&gt;</code> - URL from one of the sites listed below, e.g. <code>URL:https://arxiv.org/abs/2106.15928v1</code></li> </ul>  URLs are recognized from the following sites: <ul>     <li><a href=\"https://www.semanticscholar.org/\">semanticscholar.org</a></li>     <li><a href=\"https://arxiv.org/\">arxiv.org</a></li>     <li><a href=\"https://www.aclweb.org\">aclweb.org</a></li>     <li><a href=\"https://www.acm.org/\">acm.org</a></li>     <li><a href=\"https://www.biorxiv.org/\">biorxiv.org</a></li> </ul>
offset = 0 # int | When returning a list of results, start with the element at this position in the list. (optional) (default to 0)
limit = 100 # int | The maximum number of results to return. (optional) (default to 100)
fields = 'fields_example' # str | A comma-separated list of the fields to be returned. <br><br> The following case-sensitive citation fields are recognized: <ul>     <li><code>contexts</code></li>     <li><code>intents</code></li>     <li><code>isInfluential</code></li>     <li><code>paperId</code> - Always included</li>     <li><code>externalIds</code></li>     <li><code>url</code></li>     <li><code>title</code> - Included if no fields are specified</li>     <li><code>abstract</code></li>     <li><code>venue</code></li>     <li><code>year</code></li>     <li><code>referenceCount</code></li>     <li><code>citationCount</code></li>     <li><code>influentialCitationCount</code></li>     <li><code>isOpenAccess</code></li>     <li><code>fieldsOfStudy</code></li>     <li><code>authors</code> - Up to 500 will be returned.  Will include: <code>authorId</code> & <code>name</code></li> </ul> <br> <br> Examples: <ul>     <li>Let's suppose that the paper in the examples below has 1600 citations...</li>     <li><code>https://api.semanticscholar.org/graph/v1/paper/649def34f8be52c8b66281af98ae884c09aef38b/citations</code></li>     <ul>         <li>Returns with offset=0, next=100, and data is a list of 100 citations.</li>         <li>Each citation has a citingPaper which contains its paperId and title.</li>     </ul>     <li><code>https://api.semanticscholar.org/graph/v1/paper/649def34f8be52c8b66281af98ae884c09aef38b/citations?fields=contexts,intents,isInfluential,abstract&offset=200&limit=10</code></li>     <ul>         <li>Returns with offset=200, next=210, and data is a list of 10 citations.</li>         <li>Each citation has contexts, intents, isInfluential, and a citingPaper which contains its paperId and abstract.</li>     </ul>     <li><code>https://api.semanticscholar.org/graph/v1/paper/649def34f8be52c8b66281af98ae884c09aef38b/citations?fields=authors&offset=1500&limit=500</code></li>     <ul>         <li>Returns with offset=1500, and data is a list of the last 100 citations.</li>         <li>Each citation has a citingPaper which contains its paperId plus a list of authors</li>         <li>The authors under each citingPaper has their authorId and name.</li>     </ul> </ul> (optional)

try:
    # Details about a paper's citations
    api_response = api_instance.get_graph_get_paper_citations(paper_id, offset=offset, limit=limit, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaperApi->get_graph_get_paper_citations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paper_id** | **str**| The following types of IDs are supported: &lt;ul&gt;     &lt;li&gt;&lt;code&gt;&amp;lt;sha&amp;gt;&lt;/code&gt; - a Semantic Scholar ID, e.g. &lt;code&gt;649def34f8be52c8b66281af98ae884c09aef38b&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;CorpusId:&amp;lt;id&amp;gt;&lt;/code&gt; - Semantic Scholar numerical ID, e.g. &lt;code&gt;215416146&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;DOI:&amp;lt;doi&amp;gt;&lt;/code&gt; - a &lt;a href&#x3D;\&quot;http://doi.org\&quot;&gt;Digital Object Identifier&lt;/a&gt;,         e.g. &lt;code&gt;DOI:10.18653/v1/N18-3011&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;ARXIV:&amp;lt;id&amp;gt;&lt;/code&gt; - &lt;a href&#x3D;\&quot;https://arxiv.org/\&quot;&gt;arXiv.rg&lt;/a&gt;, e.g. &lt;code&gt;ARXIV:2106.15928&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;MAG:&amp;lt;id&amp;gt;&lt;/code&gt; - Microsoft Academic Graph, e.g. &lt;code&gt;MAG:112218234&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;ACL:&amp;lt;id&amp;gt;&lt;/code&gt; - Association for Computational Linguistics, e.g. &lt;code&gt;ACL:W12-3903&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;PMID:&amp;lt;id&amp;gt;&lt;/code&gt; - PubMed/Medline, e.g. &lt;code&gt;PMID:19872477&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;PMCID:&amp;lt;id&amp;gt;&lt;/code&gt; - PubMed Central, e.g. &lt;code&gt;PMCID:2323736&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;URL:&amp;lt;url&amp;gt;&lt;/code&gt; - URL from one of the sites listed below, e.g. &lt;code&gt;URL:https://arxiv.org/abs/2106.15928v1&lt;/code&gt;&lt;/li&gt; &lt;/ul&gt;  URLs are recognized from the following sites: &lt;ul&gt;     &lt;li&gt;&lt;a href&#x3D;\&quot;https://www.semanticscholar.org/\&quot;&gt;semanticscholar.org&lt;/a&gt;&lt;/li&gt;     &lt;li&gt;&lt;a href&#x3D;\&quot;https://arxiv.org/\&quot;&gt;arxiv.org&lt;/a&gt;&lt;/li&gt;     &lt;li&gt;&lt;a href&#x3D;\&quot;https://www.aclweb.org\&quot;&gt;aclweb.org&lt;/a&gt;&lt;/li&gt;     &lt;li&gt;&lt;a href&#x3D;\&quot;https://www.acm.org/\&quot;&gt;acm.org&lt;/a&gt;&lt;/li&gt;     &lt;li&gt;&lt;a href&#x3D;\&quot;https://www.biorxiv.org/\&quot;&gt;biorxiv.org&lt;/a&gt;&lt;/li&gt; &lt;/ul&gt; |
 **offset** | **int**| When returning a list of results, start with the element at this position in the list. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to return. | [optional] [default to 100]
 **fields** | **str**| A comma-separated list of the fields to be returned. &lt;br&gt;&lt;br&gt; The following case-sensitive citation fields are recognized: &lt;ul&gt;     &lt;li&gt;&lt;code&gt;contexts&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;intents&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;isInfluential&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;paperId&lt;/code&gt; - Always included&lt;/li&gt;     &lt;li&gt;&lt;code&gt;externalIds&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;url&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;title&lt;/code&gt; - Included if no fields are specified&lt;/li&gt;     &lt;li&gt;&lt;code&gt;abstract&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;venue&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;year&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;referenceCount&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;citationCount&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;influentialCitationCount&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;isOpenAccess&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;fieldsOfStudy&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;authors&lt;/code&gt; - Up to 500 will be returned.  Will include: &lt;code&gt;authorId&lt;/code&gt; &amp; &lt;code&gt;name&lt;/code&gt;&lt;/li&gt; &lt;/ul&gt; &lt;br&gt; &lt;br&gt; Examples: &lt;ul&gt;     &lt;li&gt;Let&#39;s suppose that the paper in the examples below has 1600 citations...&lt;/li&gt;     &lt;li&gt;&lt;code&gt;https://api.semanticscholar.org/graph/v1/paper/649def34f8be52c8b66281af98ae884c09aef38b/citations&lt;/code&gt;&lt;/li&gt;     &lt;ul&gt;         &lt;li&gt;Returns with offset&#x3D;0, next&#x3D;100, and data is a list of 100 citations.&lt;/li&gt;         &lt;li&gt;Each citation has a citingPaper which contains its paperId and title.&lt;/li&gt;     &lt;/ul&gt;     &lt;li&gt;&lt;code&gt;https://api.semanticscholar.org/graph/v1/paper/649def34f8be52c8b66281af98ae884c09aef38b/citations?fields&#x3D;contexts,intents,isInfluential,abstract&amp;offset&#x3D;200&amp;limit&#x3D;10&lt;/code&gt;&lt;/li&gt;     &lt;ul&gt;         &lt;li&gt;Returns with offset&#x3D;200, next&#x3D;210, and data is a list of 10 citations.&lt;/li&gt;         &lt;li&gt;Each citation has contexts, intents, isInfluential, and a citingPaper which contains its paperId and abstract.&lt;/li&gt;     &lt;/ul&gt;     &lt;li&gt;&lt;code&gt;https://api.semanticscholar.org/graph/v1/paper/649def34f8be52c8b66281af98ae884c09aef38b/citations?fields&#x3D;authors&amp;offset&#x3D;1500&amp;limit&#x3D;500&lt;/code&gt;&lt;/li&gt;     &lt;ul&gt;         &lt;li&gt;Returns with offset&#x3D;1500, and data is a list of the last 100 citations.&lt;/li&gt;         &lt;li&gt;Each citation has a citingPaper which contains its paperId plus a list of authors&lt;/li&gt;         &lt;li&gt;The authors under each citingPaper has their authorId and name.&lt;/li&gt;     &lt;/ul&gt; &lt;/ul&gt; | [optional]

### Return type

[**CitationBatch**](CitationBatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)

# **get_graph_get_paper_references**
> ReferenceBatch get_graph_get_paper_references(paper_id, offset=offset, limit=limit, fields=fields)

Details about a paper's references

Fetch details about the papers cited by this paper (i.e. appearing in this paper's bibliography)

### Example
```python
from __future__ import print_function
import time
import s2cholar
from s2cholar.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = s2cholar.PaperApi()
paper_id = 'paper_id_example' # str | The following types of IDs are supported: <ul>     <li><code>&lt;sha&gt;</code> - a Semantic Scholar ID, e.g. <code>649def34f8be52c8b66281af98ae884c09aef38b</code></li>     <li><code>CorpusId:&lt;id&gt;</code> - Semantic Scholar numerical ID, e.g. <code>215416146</code></li>     <li><code>DOI:&lt;doi&gt;</code> - a <a href=\"http://doi.org\">Digital Object Identifier</a>,         e.g. <code>DOI:10.18653/v1/N18-3011</code></li>     <li><code>ARXIV:&lt;id&gt;</code> - <a href=\"https://arxiv.org/\">arXiv.rg</a>, e.g. <code>ARXIV:2106.15928</code></li>     <li><code>MAG:&lt;id&gt;</code> - Microsoft Academic Graph, e.g. <code>MAG:112218234</code></li>     <li><code>ACL:&lt;id&gt;</code> - Association for Computational Linguistics, e.g. <code>ACL:W12-3903</code></li>     <li><code>PMID:&lt;id&gt;</code> - PubMed/Medline, e.g. <code>PMID:19872477</code></li>     <li><code>PMCID:&lt;id&gt;</code> - PubMed Central, e.g. <code>PMCID:2323736</code></li>     <li><code>URL:&lt;url&gt;</code> - URL from one of the sites listed below, e.g. <code>URL:https://arxiv.org/abs/2106.15928v1</code></li> </ul>  URLs are recognized from the following sites: <ul>     <li><a href=\"https://www.semanticscholar.org/\">semanticscholar.org</a></li>     <li><a href=\"https://arxiv.org/\">arxiv.org</a></li>     <li><a href=\"https://www.aclweb.org\">aclweb.org</a></li>     <li><a href=\"https://www.acm.org/\">acm.org</a></li>     <li><a href=\"https://www.biorxiv.org/\">biorxiv.org</a></li> </ul>
offset = 0 # int | When returning a list of results, start with the element at this position in the list. (optional) (default to 0)
limit = 100 # int | The maximum number of results to return. (optional) (default to 100)
fields = 'fields_example' # str | A comma-separated list of the fields to be returned. <br><br> The following case-sensitive reference fields are recognized: <ul>     <li><code>contexts</code></li>     <li><code>intents</code></li>     <li><code>isInfluential</code></li>     <li><code>paperId</code> - Always included</li>     <li><code>externalIds</code></li>     <li><code>url</code></li>     <li><code>title</code> - Included if no fields are specified</li>     <li><code>abstract</code></li>     <li><code>venue</code></li>     <li><code>year</code></li>     <li><code>referenceCount</code></li>     <li><code>citationCount</code></li>     <li><code>influentialCitationCount</code></li>     <li><code>isOpenAccess</code></li>     <li><code>fieldsOfStudy</code></li>     <li><code>authors</code> - Up to 500 will be returned.  Will include: <code>authorId</code> & <code>name</code></li> </ul> <br> <br> Examples: <ul>     <li>Let's suppose that the paper in the examples below has 1600 references...</li>     <li><code>https://api.semanticscholar.org/graph/v1/paper/649def34f8be52c8b66281af98ae884c09aef38b/references</code></li>     <ul>         <li>Returns with offset=0, next=100, and data is a list of 100 references.</li>         <li>Each reference has a citedPaper which contains its paperId and title.</li>     </ul>     <li><code>https://api.semanticscholar.org/graph/v1/paper/649def34f8be52c8b66281af98ae884c09aef38b/references?fields=contexts,intents,isInfluential,abstract&offset=200&limit=10</code></li>     <ul>         <li>Returns with offset=200, next=210, and data is a list of 10 references.</li>         <li>Each reference has contexts, intents, isInfluential, and a citedPaper which contains its paperId and abstract.</li>     </ul>     <li><code>https://api.semanticscholar.org/graph/v1/paper/649def34f8be52c8b66281af98ae884c09aef38b/references?fields=authors&offset=1500&limit=500</code></li>     <ul>         <li>Returns with offset=1500, and data is a list of the last 100 references.</li>         <li>Each reference has a citedPaper which contains its paperId plus a list of authors</li>         <li>The authors under each citedPaper has their authorId and name.</li>     </ul> </ul> (optional)

try:
    # Details about a paper's references
    api_response = api_instance.get_graph_get_paper_references(paper_id, offset=offset, limit=limit, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaperApi->get_graph_get_paper_references: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paper_id** | **str**| The following types of IDs are supported: &lt;ul&gt;     &lt;li&gt;&lt;code&gt;&amp;lt;sha&amp;gt;&lt;/code&gt; - a Semantic Scholar ID, e.g. &lt;code&gt;649def34f8be52c8b66281af98ae884c09aef38b&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;CorpusId:&amp;lt;id&amp;gt;&lt;/code&gt; - Semantic Scholar numerical ID, e.g. &lt;code&gt;215416146&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;DOI:&amp;lt;doi&amp;gt;&lt;/code&gt; - a &lt;a href&#x3D;\&quot;http://doi.org\&quot;&gt;Digital Object Identifier&lt;/a&gt;,         e.g. &lt;code&gt;DOI:10.18653/v1/N18-3011&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;ARXIV:&amp;lt;id&amp;gt;&lt;/code&gt; - &lt;a href&#x3D;\&quot;https://arxiv.org/\&quot;&gt;arXiv.rg&lt;/a&gt;, e.g. &lt;code&gt;ARXIV:2106.15928&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;MAG:&amp;lt;id&amp;gt;&lt;/code&gt; - Microsoft Academic Graph, e.g. &lt;code&gt;MAG:112218234&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;ACL:&amp;lt;id&amp;gt;&lt;/code&gt; - Association for Computational Linguistics, e.g. &lt;code&gt;ACL:W12-3903&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;PMID:&amp;lt;id&amp;gt;&lt;/code&gt; - PubMed/Medline, e.g. &lt;code&gt;PMID:19872477&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;PMCID:&amp;lt;id&amp;gt;&lt;/code&gt; - PubMed Central, e.g. &lt;code&gt;PMCID:2323736&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;URL:&amp;lt;url&amp;gt;&lt;/code&gt; - URL from one of the sites listed below, e.g. &lt;code&gt;URL:https://arxiv.org/abs/2106.15928v1&lt;/code&gt;&lt;/li&gt; &lt;/ul&gt;  URLs are recognized from the following sites: &lt;ul&gt;     &lt;li&gt;&lt;a href&#x3D;\&quot;https://www.semanticscholar.org/\&quot;&gt;semanticscholar.org&lt;/a&gt;&lt;/li&gt;     &lt;li&gt;&lt;a href&#x3D;\&quot;https://arxiv.org/\&quot;&gt;arxiv.org&lt;/a&gt;&lt;/li&gt;     &lt;li&gt;&lt;a href&#x3D;\&quot;https://www.aclweb.org\&quot;&gt;aclweb.org&lt;/a&gt;&lt;/li&gt;     &lt;li&gt;&lt;a href&#x3D;\&quot;https://www.acm.org/\&quot;&gt;acm.org&lt;/a&gt;&lt;/li&gt;     &lt;li&gt;&lt;a href&#x3D;\&quot;https://www.biorxiv.org/\&quot;&gt;biorxiv.org&lt;/a&gt;&lt;/li&gt; &lt;/ul&gt; |
 **offset** | **int**| When returning a list of results, start with the element at this position in the list. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to return. | [optional] [default to 100]
 **fields** | **str**| A comma-separated list of the fields to be returned. &lt;br&gt;&lt;br&gt; The following case-sensitive reference fields are recognized: &lt;ul&gt;     &lt;li&gt;&lt;code&gt;contexts&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;intents&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;isInfluential&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;paperId&lt;/code&gt; - Always included&lt;/li&gt;     &lt;li&gt;&lt;code&gt;externalIds&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;url&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;title&lt;/code&gt; - Included if no fields are specified&lt;/li&gt;     &lt;li&gt;&lt;code&gt;abstract&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;venue&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;year&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;referenceCount&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;citationCount&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;influentialCitationCount&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;isOpenAccess&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;fieldsOfStudy&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;authors&lt;/code&gt; - Up to 500 will be returned.  Will include: &lt;code&gt;authorId&lt;/code&gt; &amp; &lt;code&gt;name&lt;/code&gt;&lt;/li&gt; &lt;/ul&gt; &lt;br&gt; &lt;br&gt; Examples: &lt;ul&gt;     &lt;li&gt;Let&#39;s suppose that the paper in the examples below has 1600 references...&lt;/li&gt;     &lt;li&gt;&lt;code&gt;https://api.semanticscholar.org/graph/v1/paper/649def34f8be52c8b66281af98ae884c09aef38b/references&lt;/code&gt;&lt;/li&gt;     &lt;ul&gt;         &lt;li&gt;Returns with offset&#x3D;0, next&#x3D;100, and data is a list of 100 references.&lt;/li&gt;         &lt;li&gt;Each reference has a citedPaper which contains its paperId and title.&lt;/li&gt;     &lt;/ul&gt;     &lt;li&gt;&lt;code&gt;https://api.semanticscholar.org/graph/v1/paper/649def34f8be52c8b66281af98ae884c09aef38b/references?fields&#x3D;contexts,intents,isInfluential,abstract&amp;offset&#x3D;200&amp;limit&#x3D;10&lt;/code&gt;&lt;/li&gt;     &lt;ul&gt;         &lt;li&gt;Returns with offset&#x3D;200, next&#x3D;210, and data is a list of 10 references.&lt;/li&gt;         &lt;li&gt;Each reference has contexts, intents, isInfluential, and a citedPaper which contains its paperId and abstract.&lt;/li&gt;     &lt;/ul&gt;     &lt;li&gt;&lt;code&gt;https://api.semanticscholar.org/graph/v1/paper/649def34f8be52c8b66281af98ae884c09aef38b/references?fields&#x3D;authors&amp;offset&#x3D;1500&amp;limit&#x3D;500&lt;/code&gt;&lt;/li&gt;     &lt;ul&gt;         &lt;li&gt;Returns with offset&#x3D;1500, and data is a list of the last 100 references.&lt;/li&gt;         &lt;li&gt;Each reference has a citedPaper which contains its paperId plus a list of authors&lt;/li&gt;         &lt;li&gt;The authors under each citedPaper has their authorId and name.&lt;/li&gt;     &lt;/ul&gt; &lt;/ul&gt; | [optional]

### Return type

[**ReferenceBatch**](ReferenceBatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)

# **get_graph_get_paper_search**
> PaperSearchBatch get_graph_get_paper_search(query, offset=offset, limit=limit, fields=fields)

Search for papers by keyword

### Example
```python
from __future__ import print_function
import time
import s2cholar
from s2cholar.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = s2cholar.PaperApi()
query = 'query_example' # str | Search query string.  We support boolean operators OR and AND.   If you would like to ensure the inclusion of particular search terms using a MUST operator,  simply include a plus sign before the term that must be included.  For example, searching +Epidemic +Modeling +Canada will ensure each term is included in the results.  Similarly, if you'd like to ensure the exclusion of a particular search term using a MUST NOT operator, simply include a minus sign before the term that must be excluded.  For example, searching +Epidemic +Modeling +Canada -COVID will ensure each term is included in the search results but will exclude content with the negated term.  Semantic Scholar search API does not currently support wildcards. If this is a feature you would like, please let us know.
offset = 0 # int | When returning a list of results, start with the element at this position in the list. (optional) (default to 0)
limit = 100 # int | The maximum number of results to return. (optional) (default to 100)
fields = 'fields_example' # str | A comma-separated list of the fields to be returned.<br><br>  The following case-sensitive paper fields are recognized: <ul>     <li><code>paperId</code> - Always included</li>     <li><code>externalIds</code></li>     <li><code>url</code></li>     <li><code>title</code> - Included if no fields are specified</li>     <li><code>abstract</code></li>     <li><code>venue</code></li>     <li><code>year</code></li>     <li><code>referenceCount</code></li>     <li><code>citationCount</code></li>     <li><code>influentialCitationCount</code></li>     <li><code>isOpenAccess</code></li>     <li><code>fieldsOfStudy</code></li>     <li><code>authors</code> - Up to 500 will be returned</li>     <ul>         <li><code>authorId</code> - Always included</li>         <li><code>name</code> - Always included</li>     </ul> </ul> <br><br> Examples: <ul>     <li><code>https://api.semanticscholar.org/graph/v1/paper/search?query=covid+vaccination&offset=100&limit=3</code></li>     <ul>         <li>Returns with total=576278, offset=100, next=103, and data is a list of 3 papers.</li>         <li>Each paper has the always included field of paperId plus its title.  </li>     </ul>     <li><code>https://api.semanticscholar.org/graph/v1/paper/search?query=covid&fields=url,abstract,authors</code></li>     <ul>         <li>Returns with total=639637, offset=0, next=100, and data is a list of 100 papers.</li>         <li>Each paper has paperId, url, abstract, and a list of authors.</li>         <li>Each author under that list has authorId and name.</li>     </ul>     <li><code>https://api.semanticscholar.org/graph/v1/paper/search?query=totalGarbageNonsense</code></li>     <ul>         <li>Returns with total = 0, offset=0, and data is a list of 0 papers.</li>     </ul> </ul> (optional)

try:
    # Search for papers by keyword
    api_response = api_instance.get_graph_get_paper_search(query, offset=offset, limit=limit, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaperApi->get_graph_get_paper_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search query string.  We support boolean operators OR and AND.   If you would like to ensure the inclusion of particular search terms using a MUST operator,  simply include a plus sign before the term that must be included.  For example, searching +Epidemic +Modeling +Canada will ensure each term is included in the results.  Similarly, if you&#39;d like to ensure the exclusion of a particular search term using a MUST NOT operator, simply include a minus sign before the term that must be excluded.  For example, searching +Epidemic +Modeling +Canada -COVID will ensure each term is included in the search results but will exclude content with the negated term.  Semantic Scholar search API does not currently support wildcards. If this is a feature you would like, please let us know. |
 **offset** | **int**| When returning a list of results, start with the element at this position in the list. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to return. | [optional] [default to 100]
 **fields** | **str**| A comma-separated list of the fields to be returned.&lt;br&gt;&lt;br&gt;  The following case-sensitive paper fields are recognized: &lt;ul&gt;     &lt;li&gt;&lt;code&gt;paperId&lt;/code&gt; - Always included&lt;/li&gt;     &lt;li&gt;&lt;code&gt;externalIds&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;url&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;title&lt;/code&gt; - Included if no fields are specified&lt;/li&gt;     &lt;li&gt;&lt;code&gt;abstract&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;venue&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;year&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;referenceCount&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;citationCount&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;influentialCitationCount&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;isOpenAccess&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;fieldsOfStudy&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;&lt;code&gt;authors&lt;/code&gt; - Up to 500 will be returned&lt;/li&gt;     &lt;ul&gt;         &lt;li&gt;&lt;code&gt;authorId&lt;/code&gt; - Always included&lt;/li&gt;         &lt;li&gt;&lt;code&gt;name&lt;/code&gt; - Always included&lt;/li&gt;     &lt;/ul&gt; &lt;/ul&gt; &lt;br&gt;&lt;br&gt; Examples: &lt;ul&gt;     &lt;li&gt;&lt;code&gt;https://api.semanticscholar.org/graph/v1/paper/search?query&#x3D;covid+vaccination&amp;offset&#x3D;100&amp;limit&#x3D;3&lt;/code&gt;&lt;/li&gt;     &lt;ul&gt;         &lt;li&gt;Returns with total&#x3D;576278, offset&#x3D;100, next&#x3D;103, and data is a list of 3 papers.&lt;/li&gt;         &lt;li&gt;Each paper has the always included field of paperId plus its title.  &lt;/li&gt;     &lt;/ul&gt;     &lt;li&gt;&lt;code&gt;https://api.semanticscholar.org/graph/v1/paper/search?query&#x3D;covid&amp;fields&#x3D;url,abstract,authors&lt;/code&gt;&lt;/li&gt;     &lt;ul&gt;         &lt;li&gt;Returns with total&#x3D;639637, offset&#x3D;0, next&#x3D;100, and data is a list of 100 papers.&lt;/li&gt;         &lt;li&gt;Each paper has paperId, url, abstract, and a list of authors.&lt;/li&gt;         &lt;li&gt;Each author under that list has authorId and name.&lt;/li&gt;     &lt;/ul&gt;     &lt;li&gt;&lt;code&gt;https://api.semanticscholar.org/graph/v1/paper/search?query&#x3D;totalGarbageNonsense&lt;/code&gt;&lt;/li&gt;     &lt;ul&gt;         &lt;li&gt;Returns with total &#x3D; 0, offset&#x3D;0, and data is a list of 0 papers.&lt;/li&gt;     &lt;/ul&gt; &lt;/ul&gt; | [optional]

### Return type

[**PaperSearchBatch**](PaperSearchBatch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

