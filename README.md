# Pictures API

## Written in Flask, hosted via IBM Cloud Code Engine

How to Run:

1. Clone repo to your machine
2. Change to yoru project directory,
3. Run `flask run --debugger --reload`
4. Run `curl localhost:5000/health` (in a new terminal) to test the health of the application.
5. Make sure your Code Engine namespace is set to an environment variable
6. Check that you have a Code Engine namespace using `echo ${SN_ICR_NAMESPACE}` (If not, consult IBM's documentation to set one up)
7. Build a container image with `docker build -t pictures .`
8. Tag the image with `docker tag pictures us.icr.io/$SN_ICR_NAMESPACE/pictures:1`
9. Push it using `docker push us.icr.io/$SN_ICR_NAMESPACE/pictures:1`
10. Check all images in your namespace with `ibmcloud cr images --restrict $SN_ICR_NAMESPACE`
11. Deploy the image using `ibmcloud ce app create --name pictures  --image us.icr.io/${SN_ICR_NAMESPACE}/pictures:1 --registry-secret icr-secret --port 3000`
12. Double-check everything is deployed using `ibmcloud ce app get --name pictures`
