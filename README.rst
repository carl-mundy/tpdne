tpdne
#####

.. image:: https://travis-ci.com/carl-mundy/tpdne.svg?branch=master
    :target: https://travis-ci.com/carl-mundy/tpdne


Quickstart
==========

tpdne is available on PyPI and can be installed with `pip <https://pip.pypa.io>`_.

.. code-block:: console

    $ pip install tpdne

After installing tpdne you can use it like any other Python module.

Here is a simple example:

.. code-block:: python

    import tpdne
    image = tpdne.tpdne_base64()

Or, if being used within a Jupyter Notebook:

.. code-block:: python

    import tpdne
    from Ipython.display import Image

    Image(data=tpdne_base64())
