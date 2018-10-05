1. In this model inheritence, the proxy model will control the main model.
2. If we want to manage a model without hitting this model directly then we can create
   a proxy model for this model and then we can control main model.
3. We set proxy=True in meta model of new model so that this new model will become 
   proxy model to control non-abstract model.