console.log('Loading function');

exports.handler = function(event, context) {
    console.log("AutoScalingEvent()");
    console.log("Event data:\n" + JSON.stringify(event, null, 4));
    context.succeed("...");
};